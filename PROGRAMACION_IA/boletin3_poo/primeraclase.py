class Persona:
    __nombre=""

    __tlfs= set()

    def __init__(self):
        self.__nombre='Pepe'
        self.__tlfs.add("112")

    def mostrar(self):
        print("Nombre", self.__nombre)
        print("Tlfs", self.__tlfs)
    def anadirtelefono(self,tlf):
        self.__tlfs.add(tlf)

p=Persona()
p.mostrar()
p.anadirtelefono("09234u230947")
p.mostrar()