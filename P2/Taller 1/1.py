def funcion_completa():

    consonante = 'bcdfghjklmnñpqrstvxzwy'
    vocal  = 'aeiou'

    # Pedimos la palabra con la que jugaran Rodolfo y Ofelia
    pal = str(input(" ingrese la palabra con la cual concursan Rodolfo y Ofelia: "))

    # funcion para limpiar la palabra , eliminar caracteres queno sean alfanumericos, espacios vacios, y numeros 
    def limpieza_palabra(pal):
        # pone la palabra en minuscula
        pal = pal.lower()
        # borra los espacios en blanco
        pal = pal.strip()
        # borra los números
        pal = ''.join(filter(str.isalnum, pal))
        # elimiina todos los caracteres que sean numericos
        pal = ''.join([i for i in pal if not i.isdigit()])

        return pal

    # Validamos la cadena de caracteres ingresada
    palabra=limpieza_palabra(pal)


    print(f'la palabra del juego es: {palabra}\n')

    def cont_palabras(palabra,lista):

        flag= True
        flag_1=False # bandera para entrar en ciclo y reducir la palabra


        vec=[]
        while flag:
            i=0
            j=0     # Jeferson
        
            for c in lista:
                if palabra[i] == c:
                    #print(f'La palabra comienza por la consonante : {palabra[i]}')
                    # como si encontramos que la palabra comienza por una consonante entonces 
                    palabra1=palabra[i:]
                    # palabra1 es la palabra recortada de la original para comenzar a guardar en el vector
                    palabra_aux=palabra1
                    flag_1=True
                    while flag_1:
                        vec.append(palabra1)
                        palabra1=palabra1[:-1]   # eferso
                        j=j+1
                        if len(palabra_aux)==j:
                            flag_1=False

                    else:
                        break
        
            #print('ciclo termina')
            palabra=palabra[1:]      
            if len(palabra)==0:
                flag=False
                    
        x=len(vec)                
        return x
        
    rodolfo=cont_palabras(palabra,consonante)
    ofelia=cont_palabras(palabra,vocal)

    #print(rodolfo)
    #print(ofelia)
    if rodolfo>ofelia:
        texto=print(f'El ganador es rodolfo  con  {rodolfo} puntos')
    elif ofelia> rodolfo:
        texto=print(f'El ganador es ofelia con {ofelia} puntos')
    else :
        texto=print(f'Hubo Empate entre ofelia y rodolfo con {rodolfo} puntos')

    return texto


ensayo_final=funcion_completa()