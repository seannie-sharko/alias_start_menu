import json
import os
import re
import subprocess
from rich.console import Console
from rich.table import Table

ALIAS_MENU_OPTIONS_ENV = 'ALIAS_MENU_OPTIONS'
OPTION_LABELS_ENV = 'OPTION_LABELS'
OPTION_COMMANDS_ENV = 'OPTION_COMMANDS'

table = Table(title="Alias Launch Menu")
table.add_column("Alias", justify="center", style="cyan")
table.add_column("Description", justify="left", style="green")
print('\n')


def parse_env_list(env_var_name, default_values):
    raw_value = os.getenv(env_var_name, "")
    if not raw_value.strip():
        return default_values
    return [
        item.strip()
        for item in re.split(r"[\n,]+", raw_value)
        if item.strip()
    ]


def parse_json_string_map(env_var_name):
    raw_value = os.getenv(env_var_name, "")
    if not raw_value.strip():
        raise ValueError(f"{env_var_name} must be set to a JSON object")

    try:
        value_map = json.loads(raw_value)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{env_var_name} must be valid JSON") from exc

    if not isinstance(value_map, dict):
        raise ValueError(f"{env_var_name} must be a JSON object")

    invalid_entries = [
        key for key, value in value_map.items()
        if not isinstance(key, str) or not isinstance(value, str)
    ]
    if invalid_entries:
        raise ValueError(
            f"{env_var_name} keys and values must be strings: {', '.join(invalid_entries)}"
        )

    return value_map


def build_menu():
    configured_keys = parse_env_list(ALIAS_MENU_OPTIONS_ENV, DEFAULT_MENU_OPTION_KEYS)
    invalid_keys = [key for key in configured_keys if key not in OPTION_COMMANDS]
    if invalid_keys:
        raise ValueError(
            f"Invalid values in {ALIAS_MENU_OPTIONS_ENV}: {', '.join(invalid_keys)}"
        )
    missing_labels = [key for key in configured_keys if key not in OPTION_LABELS]
    if missing_labels:
        raise ValueError(
            f"Missing labels in {OPTION_LABELS_ENV}: {', '.join(missing_labels)}"
        )

    option_keys = configured_keys + ['exit']
    option_labels = {**OPTION_LABELS, 'exit': 'Exit'}
    menu = {str(index): option_labels[key] for index, key in enumerate(option_keys, start=1)}
    selection_map = {str(index): key for index, key in enumerate(option_keys, start=1)}
    return menu, selection_map


def print_menu():
    for key in menu_options.keys():
        table.add_row(key, menu_options[key])


def run_option(command):
    print('\n')
    subprocess.run(command, shell=True, check=False)
    print('\n')


OPTION_LABELS = parse_json_string_map(OPTION_LABELS_ENV)
OPTION_COMMANDS = parse_json_string_map(OPTION_COMMANDS_ENV)
DEFAULT_MENU_OPTION_KEYS = list(OPTION_COMMANDS.keys())
menu_options, menu_selection_map = build_menu()


if __name__ == '__main__':
    print_menu()
    console = Console()
    console.print(table)
    option = ''
    try:
        option = str(input('Select an alias ' + '[1 - ' + str(len(menu_options)) + ']: '))
    except:
        print('Wrong input. Please enter a number ...')
    selected_option = menu_selection_map.get(option)
    if selected_option == 'exit':
        print('Bye!')
        exit()
    elif selected_option in OPTION_COMMANDS:
        run_option(OPTION_COMMANDS[selected_option])
    else:
        print('Invalid option!')
