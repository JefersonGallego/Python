
rodolfo = 'bcdfghjklmnñpqrstvxzwy'   # Consonantes
ofelia  = 'aeiou'                    # Vocales

palabra = str(input(" Digite la Palbra del Juego: "))  # Palabra de Juego

# Arrglo Palabra
palabra = palabra.lower()                                  # Minusculas
palabra = palabra.strip()                                  # Espacios en Blanco
palabra = ''.join(filter(str.isalnum, palabra))            # Borrar Numeros
palabra = ''.join([i for i in palabra if not i.isdigit()]) # elimiina todos los caracteres que sean numericos
print(f'La Palabra es: {palabra}\n')

i = 0                   # Indice
count = 0               # Contador
puntos_ofelia = 0       # Puntaje de Ofelia
puntos_rodolfo = 0      # Puntaje de Rodolfo
flag_ofelia = False     # inicializo bandera de conteo
flag_rodolfo = False    # inicializo bandera de conteo


flag_1 = True 
while flag_1:
    
    if i == len(palabra):   # Cierro el Ciclo
         flag_1 =  False
         continue

    if i < len(ofelia):
        for v in ofelia:           # ¿Indice esta en Vocales?
            if palabra[i] == v:
                flag_ofelia = True # Bandera pa puntos de Ofelia
   
    for c in rodolfo:
        if palabra[i] == c:        # ¿Indice esta en Consonantes?
            flag_rodolfo = True    # Bandera de puntos de Rodolfo 

    
    p_formada = palabra[i:]   # Palabra Formada a partir del Indice
    p_original = p_formada    # Guardo en otra Variable paa poder comparar
    
    #print(f'\nLa palabra evaluada en el ciclo {i} es: {p_formada}\n')

    # Metodo para las frases
    flag_2 = True

    while flag_2:
        count = p_original.count(p_formada) # ¿Cuantas veces esta la Palabra Formada en la Original?

        # ¿ A quien le sumo puntos?
        
        if flag_rodolfo == True:
            puntos_rodolfo += count
            count = 0

        if flag_ofelia == True:
            puntos_ofelia += count
            count = 0

        if 1 == len(p_formada):   
            flag_ofelia = False    # Reinicio las Banderas
            flag_rodolfo = False
            flag_2 = False
            i=i+1                  # Aumento Indice

        # evaluamos el tamaño de la palabra formada
        if len(p_formada) > 0:

            p_formada = p_formada[:-1] # Reduzco Palabra, para buscar de nuevo en la Original

            
print(f' Ofelia tiene {puntos_ofelia} puntos\n')
print(f' Rodolfo tiene {puntos_rodolfo} puntos\n')
 
if puntos_rodolfo > puntos_ofelia: 
    print(f'Rodolfo es el ganador con: {puntos_rodolfo} puntos')
else: print(f'Rodolfo es el ganador con: {puntos_ofelia} puntos')