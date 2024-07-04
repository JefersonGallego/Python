# Listas
'Puedo ingresar cualquier tipo de Dato'

objeto=[7,'Hola',True,3.5]   # 7 P0,Hola P1,True P2, 3.5 P3

objeto[1]    # P1 = Hola
objeto[-3]   # Derecha Izquierda P-3 = Hola
objeto[1:3]  # Mostrar de una Posicion a otra P1 --> P3
objeto[:2]   # Mostrar de una Posicion a otra P0 --> P2
objeto[1]=4  # Sobreescribir elemnto de la lista
len(objeto)  # Longitud de la Lista
type(objeto) # Tipo 
objeto.extend(range(10,16,2)) # Incrementar la lista
objeto.count('Hola') # Cuantas veces aparec e un objeto
objeto.insert(2,3.14) # Insertar objeto en un espacio de la lista
objeto.remove('Hola') # Remover un objeto
objeto.pop(1)         # Remover posicion
objeto.append         # ingresar elemento a la lista
objeto.index(12)      # Busca el onjeto y me entrega su Posicion              
objeto.reverse()      # Invierte la posicion  de los objetos
objeto.sort()         # Organiza de Menor a Mayor
objeto.sort(reverse=True)  # Organiza de Mayor a Menor

for i in range(len(objeto)):   # Imprima Posicion y Objeto
    print([i])
    print(objeto[i])

for i in objeto:               # Imprime Cada Objeto
    print(i)

# Metodos  
print('---------------------------------------------------------')
objeto=[7,'Hola',True,False]   # 7 P0,Hola P1,True P2, 3.5 P3

print(objeto[-1:])   # Derecha Izquierda P-3 = Hola