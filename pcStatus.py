import platform
import psutil
from datetime import datetime
import os

#funções de terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def wait():
    input("\n\nPressione ENTER para continuar...\n\n")
ent = 0

#funções de psutil

while ent == 0:
    clear()
    
    print("\n\nEscolha qual status você deseja exibir: \n")
    print("01 - Informações do sistema;")
    print("02 - Informações de memória;")
    print("03 - Informações de bateria;")
    print("04 - Verificação de processos;")
    print("05 - Sair da aplicação;")
    
    choice = input('(1/2/3/4/5/6)->')
    
    if choice == '1' or choice == '01':
        clear()
        print("\n\n--INFORMAÇÕES DO SISTEMA--\n\n")
        print(f"Sistema: {platform.system} / {platform.release}")
        print(f"Versão: {platform.version}")
        print(f"Arquitetura: {platform.architecture}")
        print(f"Processador: {platform.processor}")
        print(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
        print(f"Núcleos Lógicos: {psutil.cpu_count(logical=True)}")
        print(f"Uso Atual: {psutil.cpu_percent(interval=1)}%")
        
        wait()
    elif choice == '2' or choice == '02':
        clear()
        print("\n\n-- INFORMAÇÕES DE MEMÓRIA --\n\n")
        mem = psutil.virtual_memory()
        print(f"Total: {mem.total / (1024)**3 :.2f} GB")
        print(f"Usada: {mem.used / (1024)**3 :.2f} GB")
        print(f"Livre: {mem.free / (1024)**3 :.2f} GB")
        print(f"Uso Atual: {mem.percent}%")
        wait()
    elif choice == '3' or choice == '03':
        clear()
        print("\n\n-- INFORMAÇÕES DE BATERIA --\n\n")
        bat = psutil.sensors_battery()

        if bat:
            print(f"Nível atual: {bat.percent:.2f}%")
            print(f"Status: {'Carregando' if bat.power_plugged else 'Descarregando'}")
            
            if not bat.power_plugged:
                print(f"Carga restante: {bat.secsleft // 60} min")
        else:
            print("O sistema atual não possui bateria conectada.")
        
        wait()
    elif choice == '4' or choice == '04':
        clear()
        print("\n\n--VERIFICAÇÃO DE PROCESSOS--\n\n")
        print("ID - Digite o id do processo para ver mais detalhes;")
        print("SAIR - Digite '0' para sair;")
        wait()
        leave = 0
        
        while leave == 0:            
            #Exitibir os processos
            print("\n\n-- PROCESSOS ATIVOS --\n\n")
            for search in psutil.process_iter(['pid', 'name', 'username']):
                print(f"PID: {search.info['pid']} | Nome: {search.info['name']} | Usuário: {search.info['username']}")
            
            #Escolha do usuário
            option = input("\n\n(ID/0) -> ")
            
            try:
                if option != '0':
                    pid = int(option)
                    
                    try:
                        print(f"\n\n--DETALHES DO PROCESSO {pid}--\n\n")
                        search = psutil.Process(pid)
                        print(f"Nome: {search.name()}")
                        print(f"Status: {search.status()}")
                        print(f"Craido em: {datetime.fromtimestamp(search.create_time()).strftime('%d-%m-%y %H:%M:%S')}")
                        print(f"Uso CPU: {search.cpu_percent(interval=1)}%")
                        print(f"Uso Memória: {search.memory_info().rss / (1024)**3:.2f} MB")
                        print(f"Threads: {search.num_threads()}")
                        wait()
                        
                    except psutil.NoSuchProcess:
                        print("Processo não encontrado...")
                        wait()
                elif option == '0':
                    leave = 1
                else:
                    print("Inserção inválida! Exibindo novamente...")
                    wait()
                    
            except ValueError:
                print("\n\nInserção inválida!\n\n")
                exit = 'abc'
        
                while exit != 's' and exit != 'n':
                    print("Está tentando finalizar a verificação de processos?")
                    exit = input("(s/n) -> ")
                    
                    if exit == 'n':
                        break
                    elif exit == 's':
                        leave = 1
                    else:
                        clear()
                        print("Inserção inválida!")
                        wait() 
                
    elif choice == '5' or choice == '05':
        clear()
        exit = 'abc'
        
        while exit != 's' and exit != 'n':
            print("Deseja mesmo finalizar a aplicação?")
            exit = input("(s/n) -> ")
            
            if exit == 'n':
                break
            elif exit == 's':
                ent = 1
            else:
                clear()
                print("Inserção inválida!")
                wait()      
    else:
        clear()
        print("Inserção inválida!")
        wait()

