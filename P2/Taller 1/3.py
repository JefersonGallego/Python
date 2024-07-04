from bdb import Breakpoint
from email.errors import FirstHeaderLineIsContinuationDefect
import random
import string
from pkg_resources import empty_provider

# Caracteres de Contraseña
minus= 'abcedefghijklmnopqrstuvwxyz'          # Letras Minusculas
mayus= minus.upper()                          # Letras Mayusculas
num = '1234567890'                            # Numeros
simbol= "!#$%&/()=?¡¨*[]_:;,.-{}+´¿@\`~"      # Simbolos

# Caracteres para Validad el Correo
minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
signos = ['-','.','_']
numeros = ['1','2','3','4','5','6','7','8','9','0']
dominios = ['gmail','hotmail','msn','outlook','live','yahoo']
terminar = ['com','com.co','net','es','org','gov','co']


while True:
     email= input('Digite su Email: ')                    # jefer1395 @ gmail . com
     
     if (email.find("@") or email.find(".")) != -1:      # Verfico que el correo tenga "@" y "."
          email_aux=email.split('@')                      # Divido 1 desde el @
          usuario=email_aux[0]                            # Division 1 = Usuario
          complemento=email_aux[1]                        # Division 2 = Complemento
          adicion=complemento.split('.')                  # Divido 2 desde el .
          dominio=adicion[0]                              # Division 3 = Dominios
          fin=adicion[1]                                  # Divison 4 = Terminar
          
          for x in usuario:
              if x in signos or x in numeros or x in minusculas or x in mayusculas:
                   if dominio in dominios:
                        if fin in terminar:
                             print(' Su correo es correcto ')
                             todas= minus+mayus+num+simbol          # Base para la contraseña con todos los caracteres
                             n=15                                   # 15 caracteres para la Contraseña
                             aleatorio=random.sample(todas,n)       # Crea la contraseña aletoria
                             contraseña="".join(aleatorio)          # Muestra la contraseña como un string
                             print(f'Su Correo es: {email}')
                             print('')
                             print(f'Su Contraseña es: {contraseña}')
                             print('')
                             break
                             
                        else:
                             print('El final del correo no es valido')
                        break
                                                                                                                                                
                   else:
                        print('El dominio no es valido')
                   break
                                                                        
              else:
                   print('El usuario no es valido')   
              break

     else:
          print('El correo no tiene un arroba o no tiene punto, Verifivar el caso')
     

          


