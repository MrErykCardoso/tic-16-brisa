import os

#funções de terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    input("\n\nPressione ENTER para continuar...\n\n")

#funções de edição
def create_file(fileName):
    with open(f"{fileName}.txt", "w") as arq:
        arq.write("")
        
def reset_file(fileName, content):
    with open(f"{fileName}.txt", "wt") as arq:
        arq.write(f"{content}")

def read_file(fileName):
    with open(f"{fileName}.txt", "rt") as arq:
        text = arq.read()
        print(f"\n\n{text}\n\n")
    
def write_file(fileName, content):
    with open(f"{fileName}.txt", "a") as arq:
        arq.write(f"{content}")
        
def external_edit_file(fileName):
    print("TO DO")

def exclude_file(fileName):
    print("TO DO")
    
def see_file(fileName):
    print("TO DO")
    
    
#Exceções personalizadas
class InvalidOption(Exception):
    def __init__(self, mensagem = "Inserção inválida: A inserção precisa estar dentro das opções fornecidas."):
        super().__init__(mensagem)

#Menu de exibição para o usuário
load = 1

while load == 1:
    clear()
    print("\n\n--EDITOR DE ARQUIVOS TXT--\n\n")
    print("(1) - Criar arquivo;")
    print("(2) - Resetar e escrever arquivo;")
    print("(3) - Ler arquivo;")
    print("(4) - Escrever arquivo;")
    print("(5) - Usar editor externo padrão;")
    print("(6) - Excluir arquivo;")
    print("(7) - Ver arquivos;")
    print("(8) - Finalizar editor;")
    
    try:
        option = int(input("(1,...,6) ->"))
        
        if option == 1: #Criar
            clear()
            fileName = input("\n\nInsira o nome do arquivo de texto que você deseja criar:\n-> ")
            create_file(f"./playground/{fileName}")
        
        elif option == 2: #resetar e escrever
            clear()
            print("TO DO")
        
        elif option == 3: #Ler
            clear()
            print("TO DO")
        
        elif option == 4: #Escrever
            clear()
            print("TO DO")
        
        elif option == 5: #editor externo
            clear()
            print("TO DO")
        
        elif option == 6: #excluir
            clear()
            print("TO DO")
        
        elif option == 7: #ver
            clear()
            print("TO DO")
        
        elif option == 8: #sair
            clear()
            exit = 0
            
            while exit == 0:
                clear()
                print("\n\nDeseja mesmo sair da aplicação?\n")
                option = input("(s/n) -> ")
                
                if option == 's':
                    load = 0
                    exit = 1
                elif option == 'n':
                    exit = 1
                else:
                    print("Inserção incorreta: A inserção deve estar dentro das opções fornecidas.")
                    wait()
        
        else:
            raise InvalidOption()
        
    except ValueError as e:
        print(f"Erro: {e}\n Mensagem: A entrada deve ser numérica e estar dentro das opções fornecidas.")
        wait()
    except InvalidOption as e:
        print(f"Erro: {e}")
        wait()
    finally:
        wait()

