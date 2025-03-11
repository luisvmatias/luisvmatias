import os
from datetime import datetime
from colorama import init, Fore, Style
import re
import time  # Para dar intervalo na verificação das rotinas

init(autoreset=True)
routines = {}

def load_routines():
    if os.path.exists('routines.txt'):
        with open('routines.txt', 'r') as file:
            for line in file:
                if '|' in line:
                    try:
                        name, routine_time = line.strip().split('|')
                        routines[name] = routine_time
                    except ValueError:
                        continue  # Ignora linhas mal formatadas

def save_routines():
    with open('routines.txt', 'w') as file:
        for name, routine_time in routines.items():
            file.write(f'{name}|{routine_time}\n')

def show_routines():
    if not routines:
        print(Fore.RED + 'Nenhuma rotina encontrada.')
    else:
        print(Fore.CYAN + '\nSuas rotinas:')
        for name, time in routines.items():
            print(Fore.GREEN + f'• {name} - Horário: {time}')

def validate_time(time_str):
    """Valida se o horário está no formato HH:MM."""
    return bool(re.match(r"^([01]?[0-9]|2[0-3]):([0-5][0-9])$", time_str))

def add_routine():
    name = input(Fore.YELLOW + 'Digite o nome da rotina: ')
    while True:
        time_str = input(Fore.YELLOW + 'Digite o horário da rotina (HH:MM): ')
        if validate_time(time_str):
            break
        else:
            print(Fore.RED + 'Formato de horário inválido. Por favor, insira no formato HH:MM.')
    routines[name] = time_str
    print(Fore.GREEN + '✔️ Rotina adicionada com sucesso!')

def remove_routine():
    show_routines()
    name = input(Fore.YELLOW + 'Digite o nome da rotina que deseja remover: ')
    if name in routines:
        del routines[name]
        print(Fore.GREEN + '✔️ Rotina removida com sucesso!')
    else:
        print(Fore.RED + 'Rotina não encontrada.')

def check_routines():
    now = datetime.now().strftime('%H:%M')
    for name, time in routines.items():
        if time == now:
            print(Fore.MAGENTA + f'🔔 Hora de: {name} (Agora são {now})')

def main():
    load_routines()
    while True:
        check_routines()
        print(Fore.MAGENTA + '\n--- Gerenciador de Rotinas ---')
        print(Fore.CYAN + '1. Ver rotinas')
        print(Fore.CYAN + '2. Adicionar rotina')
        print(Fore.CYAN + '3. Remover rotina')
        print(Fore.CYAN + '4. Sair')
        choice = input(Fore.YELLOW + 'Escolha uma opção: ')

        if choice == '1':
            show_routines()
        elif choice == '2':
            add_routine()
            save_routines()
        elif choice == '3':
            remove_routine()
            save_routines()
        elif choice == '4':
            save_routines()
            print(Fore.GREEN + 'Saindo... Até mais!')
            break
        else:
            print(Fore.RED + 'Opção inválida. Tente novamente.')
        
        # Aguardar 60 segundos antes de verificar as rotinas novamente
        time.sleep(0)

if __name__ == '__main__':
    main()
