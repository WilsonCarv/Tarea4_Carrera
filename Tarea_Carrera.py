class Vehiculo:
    fuerzaDelMotor=0
    def __init__(self):
        print("Creando un vehiculo")


    def Avanzar(self):
        print("Estoy avanzando")
import random
class camion(Vehiculo):
    def __init__(self):
        super().__init__()
        self.fuerzaDelMotor= random.randint(0, 9)
    def Avanzar(self):
         return 2*(self.fuerzaDelMotor)+1
import  math
class tractor(Vehiculo):
    def __init__(self):
        super().__init__()
        self.fuerzaDelMotor= random.randint(0, 9)
    def Avanzar(self):
         return int(math.log(2)* self.fuerzaDelMotor)
class sedan(Vehiculo):
    def __init__(self):
        super().__init__()
        self.fuerzaDelMotor= random.randint(0, 9)
    def Avanzar(self):
         return 3*(self.fuerzaDelMotor**2)
class bus(Vehiculo):
    def __init__(self):
        super().__init__()
        self.fuerzaDelMotor= random.randint(0, 9)
    def Avanzar(self):
         return 2*self.fuerzaDelMotor
miCamion = camion()
miTractor= tractor()
miSedan= sedan()
miBus = bus()
AvanceCamion=0
AvanceTractor=0
AvanceSedan=0
AvanceBus=0
Contador = 0
while AvanceCamion < 1000 and AvanceTractor < 1000 and AvanceSedan < 1000 and AvanceBus < 1000:
    AvanceCamion = AvanceCamion +  miCamion.Avanzar()
    AvanceTractor = AvanceTractor + miTractor.Avanzar()
    AvanceSedan = AvanceSedan + miSedan.Avanzar()
    AvanceBus = AvanceBus + miBus.Avanzar()

    lista = [AvanceCamion,AvanceTractor,AvanceSedan,AvanceBus]
    mayor = max(lista)
    Contador = Contador + 1
    if(mayor>= 1000):
        break


print(lista)
print("El total de ciclos es de" , Contador)