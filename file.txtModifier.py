import os

#funções de terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    input("\n\nPressione ENTER para continuar...\n\n")

def path(fileName):
    path = f"./playground/{fileName}.txt"
    return path

#funções de edição
def create_file(path):
    with open(f"{path}", "w") as arq:
        arq.write("")
    print("Arquivo criado com sucesso!")
    return      
def reset_file(path, content):
    with open(f"{path}", "wt") as arq:
        arq.write(f"{content}")
    print(f"Arquivo resetado e conteúdo adicionado: '{content}'")
    return
def read_file(path):
    with open(f"{path}", "rt") as arq:
        text = arq.read()
        print(f"\n\nConteúdo do aqrquivo:\n{text}\n\n")
    return    
def write_file(path, content):
    with open(f"{path}", "a") as arq:
        arq.write(f"\n\n{content}")
    print(f"Conteúdo adicionado ao arquivo: '{content}'")
    return
def external_edit_file(path):
    os.system(f"start '' '{path}'" if os.name == "nt" else f"''xdg-open '{path}'")
    return
def exclude_file(path):
    os.remove(f"{path}")
    return
def see_file(path):
    files = os.listdir(f"{path}")
    txtFiles = [f for f in files if f.endswith(".txt")]
    if txtFiles:
        print
        cont = 1
        for txt in txtFiles:
            print(f"#{cont}: {txt}")
            cont+=1
        return
    else:
        print("Nenhum arquivo .txt encontrado.")
        return        

#Exceções personalizadas
class InvalidOption(Exception):
    def __init__(self, mensage = "Inserção inválida: A inserção precisa estar dentro das opções fornecidas."):
        super().__init__(mensage)
class ExecutionFail(Exception):
    def __init__(self, mensage = "Falha ao tentar abrir o EDITO DE TEXTO EXTERNO."):
        super().__init__(mensage)
class CreationFail(Exception):
    def __init__(self, mensage = "Falha ao CRIAR arquivo de texto."):
        super().__init__(mensage)
class ResetFail(Exception):
    def __init__(self, mensage = "Falha ao RESETAR o arquivo"):
        super().__init__(mensage)
class ReadFail(Exception):
    def __init__(self, mensage = "Falha ao LER o arquivo"):
        super().__init__(mensage)
class WriteFail(Exception):
    def __init__(self, mensage = "Falha ao ESCREVER o arquivo"):
        super().__init__(mensage)  
class ExclusionFail(Exception):
    def __init__(self, mensage = "Falha ao EXCLUIR o arquivo: arquivo inexistente."):
        super().__init__(mensage)
class SeeFail(Exception):
    def __init__(self, mensage = "Falha ao  VER arquivos: A pasta raiz 'playground' inexitente."):
        super().__init__(mensage)

#Menu de exibição para o usuário
load = 1
if not os.path.exists("./playground"):
    os.makedirs("./playground")

while load == 1:    
    clear()
    print("\n\n--EDITOR DE ARQUIVOS TXT--\n\n")
    print("(1) - Criar arquivo;")
    print("(2) - Resetar e escrever arquivo;")
    print("(3) - Ler arquivo;")
    print("(4) - Escrever arquivo;")
    print("(5) - Usar editor externo padrão;")
    print("(6) - Excluir arquivo;")
    print("(7) - Listar arquivos;")
    print("(8) - Finalizar editor;")
    
    try:
        option = int(input("(1,...,6) -> "))
        
        if option == 1:   #Criar
            clear()
            print("\n\n--CRIAR ARQUIVO--\n\n")
            fileName = input("\n\nInsira o nome do arquivo de texto que você deseja criar:\n-> ")
            try:
                create_file(path(fileName))                
            except CreationFail as e:
                print(f"Error: {e}")
        elif option == 2: #resetar e escrever
            clear()
            print("\n\n--RESETAR E ESCREVER ARQUIVO--\n\n")
            fileName = input("\n\nInsira o nome do arquivo de texto que você deseja SOBRESCREVER:\n-> ")
            content = input("Insira o conteúdo para adicionar no arquivo:\n-> ")
            try:
                reset_file(path(fileName), content)
            except ResetFail as e:
                print(f"Error: {e}")
        elif option == 3: #Ler
            clear()
            print("\n\n--LER ARQUIVO--\n\n")
            fileName = input("\n\nInsira o nome do arquivo de texto que você deseja LER:\n-> ")
            try:
                read_file(path(fileName))
            except ReadFail as e:
                print(f"Error: {e}")
        elif option == 4: #Escrever
            clear()
            print("\n\n--ESCREVER ARQUIVO--\n\n")
            fileName = input("\n\nInsira o nome do arquivo de texto que você deseja ESCREVER:\n-> ")
            content = input("Insira um conteúdo para adicionar no arquivo:\n-> ")
            try:
                write_file(path(fileName), content)
            except WriteFail as e:
                print(f"Error: {e}")          
        elif option == 5: #editor externo
            clear()
            print("\n\n--USAR EDITOR EXTERNO PADRÃO--\n\n")
            fileName = input("Insira o nome do arquivo que deseja editar:\n-> ")
            try:
                external_edit_file(path(fileName))
            except ExecutionFail as e:
                print(f"Error: {e}")
        elif option == 6: #excluir
            clear()
            print("\n\n--EXCLUIR ARQUIVO--\n\n")
            fileName = input("\n\nInsira o nome do arquivo de texto que você deseja EXCLUIR:\n-> ")
            try:
                exclude_file(path(fileName))
            except ExclusionFail as e:
                print(f"Error: {e}")        
        elif option == 7: #Listar Arquivos
            clear()
            print("\n\n--LISTAR ARQUIVOS--\n\n")
            print("Imprimindo arquivos da pasta raiz:")
            try:
                see_file("./playground")
            except SeeFail as e:
                print(f"Error: {e}")  
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
        clear()
        print(f"Erro: {e}\n Mensagem: A entrada deve ser numérica e estar dentro das opções fornecidas.")
    except InvalidOption as e:
        clear()
        print(f"Erro: {e}")
    finally:
        wait()

