orden = bool (input(""""Defina el Orden Deseado     
    
    False = Asendete
    True  = Descendente
    
    Digita tu Opcion: """))   # Bool Reconocer si es T o F

lista=[]
for i in range(10):
    lista.append(float(input("Digite el Numero: ")))          # Adiciona Datos

lista.sort(reverse=orden)
print(lista)

for _ in range(10):      # Guion bajo si no hay la Necesiada de una I
    lista.append(float(input("Digite el Numero: ")))          # Adiciona Datos

lista.sort(reverse=orden)
print(lista)
