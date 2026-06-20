# Alias Start Menu

`alias_start_menu` is a small terminal menu for launching shell commands by number.

The menu is fully driven by environment variables:

- `OPTION_LABELS` controls the text shown in the menu
- `OPTION_COMMANDS` controls the command run for each menu item
- `ALIAS_MENU_OPTIONS` controls the order of items in the menu

The script prints a numbered table with `rich`, waits for a selection, then runs the matching command with `subprocess.run(..., shell=True)`.

## Requirements

- Python 3
- `rich`

Install dependencies with:

```bash
pip install rich
```

## Environment variables

### `OPTION_LABELS`

A required JSON object mapping stable option keys to the text shown in the menu.

Example:

```bash
export OPTION_LABELS='{
  "task_alpha": "Run Task Alpha",
  "task_beta": "Run Task Beta",
  "task_gamma": "Run Task Gamma",
  "task_delta": "Run Task Delta"
}'
```

### `OPTION_COMMANDS`

A required JSON object mapping the same option keys to shell commands.

Example:

```bash
export OPTION_COMMANDS='{
  "task_alpha": "${APP_BIN_DIR}/task_alpha.sh",
  "task_beta": "source ${VENV_DIR}/bin/activate && python3 ${SCRIPT_DIR}/task_beta.py",
  "task_gamma": "source ${VENV_DIR}/bin/activate && python3 ${SCRIPT_DIR}/task_gamma.py --verbose",
  "task_delta": "${APP_BIN_DIR}/task_delta.sh --dry-run"
}'
```

### `ALIAS_MENU_OPTIONS`

An optional ordered list of option keys to show in the menu.

If it is unset, the script uses the key order from `OPTION_COMMANDS`.

It supports either:

- comma-separated values
- newline-separated values

Multiline example:

```bash
export ALIAS_MENU_OPTIONS='
task_alpha
task_beta
task_gamma
task_delta
'
```

## Running the script

Run:

```bash
python aliases.py
```

The script appends an `Exit` entry automatically.

## Example output

```text
            Alias Launch Menu
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Alias ┃ Description                   ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   1   │ Run Task Alpha                │
│   2   │ Run Task Beta                 │
│   3   │ Run Task Gamma                │
│  ...  │ ...                           │
│   5   │ Exit                          │
└───────┴───────────────────────────────┘
Select an alias [1 - 5]:
```

## Validation behavior

The script fails fast when:

- `OPTION_LABELS` is missing
- `OPTION_COMMANDS` is missing
- either JSON object is invalid
- keys or values in those JSON objects are not strings
- `ALIAS_MENU_OPTIONS` contains a key missing from `OPTION_COMMANDS`
- `ALIAS_MENU_OPTIONS` contains a key missing from `OPTION_LABELS`

## Notes

- Commands are executed with `subprocess.run(command, shell=True, check=False)`.
- Because commands are shell strings, shell features such as `&&` and variable expansion are allowed.
- `OPTION_LABELS` and `OPTION_COMMANDS` should use the same set of keys.

## Project layout

- [aliases.py](/Users/sean/PycharmProjects/git_projects/alias_start_menu/aliases.py): main script
- [README.md](/Users/sean/PycharmProjects/git_projects/alias_start_menu/README.md): project documentation
