lista1=list(range(10))
l2=[i*10 for i in lista1]            # Mutiplico todos los elemento de Lista1 por i=10
l2
l2=[i*(i-1) for i in lista1]
l2
lpar=[i for i in lista1 if i%2==0]   # Con condiciones: Solo mostrar los numeros pares
lpar
lista = ['casa','perro','puerta']
lista
cap=[palabra.capitalize() for palabra in lista]