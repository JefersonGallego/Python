from cmath import pi


class Cilindro:

    # Constructor
    def __init__(self,radio,height,color='Azul'): #Color por defecto
        self.radio=radio
        self.height=height
        self.color=color

    # Metodos de Instancia
    def perimeter(self):
        return 2*self.radio*self.height
    
    
    @property
    def area_base(self):
        return pi*self.radio**2
    
    @area_base.setter  # Deja al usuario modificar la propiedad
    def area_base(self,area_base):
        # A= Pi*r**2
        # r = (A/Pi)}**0.5
        if area_base<=0:
            raise ValueError ('El Area no puede ser cero o negativa')
        #self.radio= (area/base)*pi

    
    def volumen(self):
        return pi*self.radio**2*self.height
    
    def __str__(self,):
        return (f'Radiip={self.radio}')

    # Metodos Estaticos
    @staticmethod # Decorador
    def are_equal_height(cilindro1,cilindro2):
        if cilindro1.height == cilindro2.height:
            return True
        return False
    
    # Metodos de Claes
    @classmethod # Decorados
    def tank_cilinder(cls):
        radio=2
        heigth=3
        color= 'AZUL'
        return cls(radio,heigth,color)
         

# Creso Objeto

if __name__=='__main__':

        
    cilindro3=Cilindro.tank_cilinder()
    print(cilindro3)
    
    cil1=Cilindro(3,5,'Rojo')
    cil2= Cilindro(1,2+3)
    print(f'SON LOS CILINDROS iGUALES = {Cilindro.are_equal_height(cil1,cil2)}')
   
    cilindro=Cilindro(2,4)
    print(f'El perimetro del cilindro es {cilindro.perimeter()}')   # Metodo ()
    #print(f'El are de la base del cilindro es {cilindro.area_base()}')
    print(f'El volumen del cilindro es {cilindro.volumen()}')
    print(f'El color del cilindro es {cilindro.color}')             # Atributos
    

