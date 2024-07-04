# ADIVINA EL NUMERO
import random

## Funcion Principal
def main():
    numero_aletorio= random.randint(1,100)
    numero_usuario=int(input('Elija un Numero etre el 1 al 100 : '))
    while numero_aletorio != numero_usuario:
        if numero_usuario<numero_aletorio:
            print('Piemsa en un numero mayor...')
        elif numero_usuario>numero_aletorio:
            print('Piemsa en un numero menor...')   
        else:
            print('Debes digitar un nuero entre 1 - 100...')
    
    print('Has Ganado')

if __name__=='__main__':
    main()