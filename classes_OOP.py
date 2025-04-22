class usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mensagem(self):
        return f"Meu nome é {self.nome} e minha idade é {self.idade}."
    
pessoa1 = usuario('Marcelo', 25)
pessoa2 = usuario('Milenna', 24)

#print (f"Meu nome é {pessoa1.nome} e minha namorada gatinha se chama {pessoa2.nome}. Nossas idade são respectivamente {pessoa1.idade} e {pessoa2.idade} anos. <3")

class banco:
    
    def __init__(self, saldo):
        self.saldo = saldo
    
    def getSaldo(self):
        return f"Saldo: {self.saldo} R$"
        
    def deposito(self, valorDeposito):
        self.saldo = self.saldo + valorDeposito
        print(f"Depósito de {valorDeposito} R$ efetuado!")
        
    def saque(self, valorSaque):
        if self.saldo >= valorSaque:
            self.saldo = self.saldo - valorSaque
            print(f"Saque de {valorSaque} R$ efetuado!")
        else:
            print(f"Saldo insuficiente: {self.saldo}")
    
#nubank.deposito(500)
#print(f"Saldo no seu NuBank:\n{nubank.getSaldo()}")
#nubank.saque(50)
#print(f"Saldo no seu NuBank:\n{nubank.getSaldo()}")
#nubank.saque(1452)

class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
class carro(veiculo):
    
    def __init__(self, marca, modelo, motor, cor, placa, ano):
        super().__init__(marca, modelo)
        self.motor = motor
        self.cor = cor
        self.placa = placa
        self.ano = ano
        
    def getCarro(self):
        return print(f"Informações do carro:\nMarca: {self.marca};\nModelo: {self.modelo};\nMotor: {self.motor}\nCor: {self.cor};Placa: {self.placa}\nAno: {self.ano}")

Mille = carro('Fiat', 'Mille Way Econnomy', 'Fire 1.0', 'Prata', 'YM3Z90', 2013)
#Mille.getCarro()

class animal:
    def falar(self):
        pass

class gato(animal):
    def __init__(self):
        super().__init__()
    
    def falar(self):
        print("Miau")
        
class cachorro(animal):
    def __init__(self):
        super().__init__()
        
    def falar(self):
        print("Au AU!")
