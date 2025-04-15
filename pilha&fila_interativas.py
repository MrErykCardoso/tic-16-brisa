import os

tarefa = "Tarefa: faça uma lista e uma pilha funcionais"

print(tarefa)

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n\n")
    
def espera():
    input("\n\nPressione ENTER para continuar...\n\n")

def adicionar(indice, lista ):
    lista.append(indice)
    return lista

def remover_pilha(lista):
    if len(lista) > 0:
        lista.pop()
    else:
        print("\nA pilha já está vazia!\n")
        
    return lista

def remover_fila(lista):
    if len(lista) > 0:
        lista.pop(0)
    else:
        print("\nA fila já está vazia.\n")
        
    return lista

def ver_lista(lista):
    if len(lista) > 0:
        print(lista)
    else:
        print("\nNada foi inserido ainda...\n")
    
def limpar_lista(lista):
    if len(lista) == 0:
        print("\nNada foi inserido ainda...\n")
    else:
        lista.clear()
    
    return lista

lista1 = []
lista2 = []

while True:
    limparTerminal()    
    escolha = input("\nEscolha qual estrutura de armazenamento você deseja editar:\n(1) Pilha\n(2) Fila\n(sair)\n\n->")

    #Pilha
    if escolha == '1':
        while True:
            limparTerminal()
            operacao = input("\nOperações com PILHA:\nQual operação você deseja realizar?\n(1) Adicionar elemento\n(2) Remover topo\n(3) Ver Pilha\n(4) Limpar Pilha\n(sair)\n\n-> ")
            
            if operacao == '1':
                limparTerminal()
                add = input("\nQual elemento você deseja adicionar na lista?\n\n-> ")
                lista1 = adicionar(add, lista1)
                print("\nElemento adicionado com sucesso!\n")
                espera()
            
            elif operacao == '2':
                limparTerminal()
                print("\nRemovendo topo da pilha...\n")
                lista1 = remover_pilha(lista1)
                print("\nConcluído.\n")
                espera()                
            
            elif operacao == '3':
                limparTerminal()
                print("\nImprimindo Pilha...\n")
                ver_lista(lista1)
                espera()
            
            elif operacao == '4':
                limparTerminal()
                print("\nLimpando pilha...\n")
                lista1 = limpar_lista(lista1)
                print("\nConcluído.\n")
                espera()
            
            elif operacao == 'sair':
                break
            
            else:
                limparTerminal()
                print("\nInserção incorreta! Reiniciando...\n")
                espera()
            
            
        
    #Fila
    elif escolha == '2':
        while True:
            limparTerminal()
            operacao = input("\nOperações com FILA:\nQual operação você deseja realizar?\n(1) Adicionar elemento\n(2) Remover primeiro da Fila\n(3) Ver Fila\n(4) Limpar Fila\n(sair)\n\n-> ")
            
            if operacao == '1':
                limparTerminal()
                add = input("\nQual elemento você deseja adicionar na Fila?\n\n-> ")
                lista2 = adicionar(add, lista2)
                print("\nElemento adicionado com sucesso!\n")
                espera()
            
            elif operacao == '2':
                limparTerminal()
                print("\nRemovendo o primeiro da Fila...\n")
                lista2 = remover_fila(lista2)
                print("\nConcluído.\n")
                espera()                
            
            elif operacao == '3':
                limparTerminal()
                print("\nImprimindo Fila...\n")
                ver_lista(lista2)
                espera()
            
            elif operacao == '4':
                limparTerminal()
                print("\nLimpando Fila...\n")
                lista2 = limpar_lista(lista2)
                print("\nConcluído.\n")
                espera()
            
            elif operacao == 'sair':
                break
            
            else:
                limparTerminal()
                print("\nInserção incorreta! Reiniciando...\n")
                espera()
    #Sair
    elif escolha == 'sair':
        break
    
    #Exceção
    else:
        limparTerminal()
        print("\nInserção incorreta! Reiniciando...\n")
        espera()
    