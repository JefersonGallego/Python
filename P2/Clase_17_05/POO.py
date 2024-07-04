# PROGRAMACION ORIENTADA A OBJETOS

class Laptop:
    """""
    Clase empleada para trabajar con Laptops
    """""
    #Metodo Constructor
    def __init__(self,marca,procesador,memoria,ssd):
        self.marca=marca
        self.procesador=procesador
        self.memoria=memoria
        self.has_ssd=ssd

    #Metodo Destructor
    def __del__(self):
        print('Se a eliminado el laptop')

if __name__ =='__main__':
    laptop1=Laptop('Dell','Core_17',16,True)       # Instacionando Objeto

    print(laptop1)
    print(laptop1.__dict__)
