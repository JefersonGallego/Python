

class Polygon: # Clase Padre
    
    # Constructor
    def __init__(self,number_sides):
        self.number_sides = number_sides
        self.sides= [0]*number_sides

    # Intancias
    def input_sides(self):
        self.sides=[float(input(f'Side{i+1}: ')) for i in range(self.number_sides)]
    
    def disp_sides(self):
        for i in range(self.number_sides):
            print(f'the side {i+1} is {self.sides[i]}')

class Triangle(Polygon):      # Tringle hijo de Polygon

    def __init__(self):
        super().__init__(3)
    
    def find_area(self):
        a,b,c=self.sides
        # Calculate the semi_perimeter
        s=(a+b+c)/2
        # Metodo de Eron
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print(f'Tha area is {area}')


if __name__=='__main__':

    poly=Polygon(4)
    poly.input_sides()
    poly.disp_sides()

   t1=Triangle()
   t1.input_sides()
   t1.disp_sides()
   t1.find_area()
