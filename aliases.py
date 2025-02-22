import os
from rich.console import Console
from rich.table import Table

SHELL_DIR = '/Users/$USER/scripts/sh'
PY_VIRT_DIR = f"source /Users/{os.environ['USER']}/py_venv/dev/bin/activate"
PY_SCRIPT_DIR = f"/Users/{os.environ['USER']}/scripts/python"
PY_VER = 'python3'
EXIT = 'deactivate'

menu_options = {
    '1': 'Start All Torrents',
    '2': 'Status of Incomplete Torrents',
    '3': 'Status of All Torrents',
    '4': 'Clean Torrent Directories',
    '5': 'Locate Duplicate Movies',
    '6': 'Reload Zsh',
    '7': 'Show All DNS Records',
    '8': 'Restart VM',
    '9': 'Backup VM',
    '10': 'Start VM',
    '11': 'Backup Prom Config',
    '12': 'Show Recent Spotify Tracks',
    '13': 'Update All RPis',
    '14': 'Recent PiHole Blocks',
    '15': 'Tail Ansible',
    '16': 'Jellyfin Event Log',
    '17': 'Tail Untangle',
    '18': 'Wireless Status',
    '19': 'Switch Status',
    '20': 'Mount NAS Drives',
    '21': 'Exit',
}

table = Table(title="Alias Launch Menu")
table.add_column("Alias", justify="center", style="cyan")
table.add_column("Description", justify="left", style="green")
print('\n')

def print_menu():
    for key in menu_options.keys():
        table.add_row(key, menu_options[key])

def option1():
    print('\n')
    os.system(f"{SHELL_DIR}/start_all_torrents.sh")
    print('\n')

def option2():
    print('\n')
    os.system(f"{SHELL_DIR}/status_of_incomplete_torrents.sh")
    print('\n')

def option3():
    print('\n')
    os.system(f"{PY_VIRT_DIR} && {PY_VER} {PY_SCRIPT_DIR}/transmission_status.py && {EXIT}")
    print('\n')

def option4():
    print('\n')
    os.system(f"{SHELL_DIR}/clean_torrent_directories.sh")
    print('\n')

def option5():
    print('\n')
    os.system(f"{SHELL_DIR}/locate_duplicate_movies.sh")
    print('\n')

def option6():
    print('\n')
    os.system(f"{SHELL_DIR}/reload_zsh.sh")
    print('\n')

def option7():
    print('\n')
    os.system(f"{SHELL_DIR}/show_all_dns_records.sh")
    print('\n')

def option8():
    print('\n')
    os.system(f"{SHELL_DIR}/restart_vm.sh")
    print('\n')

def option9():
    print('\n')
    os.system(f"{SHELL_DIR}/backup_vm.sh")
    print('\n')

def option10():
    print('\n')
    os.system(f"{SHELL_DIR}/start_vm.sh")
    print('\n')

def option11():
    print('\n')
    os.system(f"{SHELL_DIR}/backup_prom_config.sh")
    print('\n')

def option12():
    print('\n')
    os.system(f"{PY_VIRT_DIR} && {PY_VER} {PY_SCRIPT_DIR}/recent_tracks.py && {EXIT}")
    print('\n')

def option13():
    print('\n')
    os.system(f"{SHELL_DIR}/update_all_rpis.sh")
    print('\n')

def option14():
    print('\n')
    os.system(f"{SHELL_DIR}/pihole_blocks.sh")
    print('\n')

def option15():
    print('\n')
    os.system(f"{SHELL_DIR}/tail_ansible.sh")
    print('\n')

def option16():
    print('\n')
    os.system(f"{PY_VIRT_DIR} && {PY_VER} {PY_SCRIPT_DIR}/jellyfin_activity.py && {EXIT}")
    print('\n')

def option17():
    print('\n')
    os.system(f"{SHELL_DIR}/untangle_query.sh")
    print('\n')

def option18():
    print('\n')
    os.system(f"{PY_VIRT_DIR} && {PY_VER} {PY_SCRIPT_DIR}/wireless.py && {EXIT}")
    print('\n')

def option19():
    print('\n')
    os.system(f"{PY_VIRT_DIR} && {PY_VER} {PY_SCRIPT_DIR}/switches.py && {EXIT}")
    print('\n')

def option20():
    print('\n')
    os.system(f"{SHELL_DIR}/nas.sh")
    print('\n')

if __name__ == '__main__':
    print_menu()
    console = Console()
    console.print(table)
    option = ''
    try:
        option = str(input('Select an alias ' + '[1 - ' + str(len(menu_options)) + ']: '))
    except:
        print('Wrong input. Please enter a number ...')
    if option == '1':
        option1()
    elif option == '2':
        option2()
    elif option == '3':
        option3()
    elif option == '4':
        option4()
    elif option == '5':
        option5()
    elif option == '6':
        option6()
    elif option == '7':
        option7()
    elif option == '8':
        option8()
    elif option == '9':
        option9()
    elif option == '10':
        option10()
    elif option == '11':
        option11()
    elif option == '12':
        option12()
    elif option == '13':
        option13()
    elif option == '14':
        option14()
    elif option == '15':
        option15()
    elif option == '16':
        option16()
    elif option == '17':
        option17()
    elif option == '18':
        option18()
    elif option == '19':
        option19()
    elif option == '20':
        option20()
    elif option == '21':
        print('Bye!')
        exit()
    else:
        print('Invalid option!')
