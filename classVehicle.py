from abc import ABC, abstractmethod

#classe com métodos e atributos abstratos para servir como interface
@abstractmethod
class Ivehicle(ABC):
    @abstractmethod
    def __init__(self, branch, model):
        super().__init__()
        self.branch
        self.model        
    
    @abstractmethod
    def accelerate():
        pass
    
    @abstractmethod
    def stop():
        pass

#classe pai ou superclasse que determina atributos e métodos básicos
class Vehicle(Ivehicle):
    def __init__(self, branch, model):
        super().__init__(branch, model)
        self.branch = branch
        self.model = model
        
    def accelerate():
        print("vruuuuuuuuuuuuum - som do motor acelerando!")
        
    def stop():
        print("Nhiiiiiiiiiiiiii - som do veículo desacelerando!")

#subclasse que herda atributos e métodos básicos, mas contem atributos e métodos nichados
class SuperVehicle(Vehicle):
    def __init__(self, marca, modelo, engine, chassis):
        super().__init__(marca, modelo)
        self.__marca = marca
        self.__modelo = modelo
        self.__engine = engine
        self.__chassis = chassis
        
    def __accelerate():
        print("dram dan dan vruuuuuuuuuuuuum - som do motor acelerando ferozmente!")
    
    def __stop():
        print("Nhi Nhi Nhiiiiiiiiiiiiii - som do veículo desacelerando com impeto!")
        
    def get_info(self):
        return f"Marca: {self.__marca} | Modelo: {self.__modelo} | Engine: {self.__engine} | Chassis: {self.__chassis}"
    
    def get_accelerate(self):
        return self.__accelerate()
    
    def get_stop(self):
        return self.__stop()
    
def displayInformation(SuperVehicle):
    SuperVehicle.get_info()
    SuperVehicle.get_accelerate()
    SuperVehicle.get_stop()

        
    