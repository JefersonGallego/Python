

class A:
    
    def __init__(self):
        print('Soy la clas A')
    def a(self):
        print('Metodo heredado de A')

class B:
    
    def __init__(self):
        print('Soy la clas B')
    def b(self):
        print('Metodo heredado de B')

class C(B,A):     #C hija de A y B
    def v(self):
        print('Metodo de C')


if __name__=='__main__':
    c=C()
   
    c.a()  # Metodo de la clase a
    c.b()  # Metodo de la clase b
    


