
#import matplotlib.pyplot as plt

diccionario={'int':7,'str':'Hola','bool':True,'float':3.5}
diccionario={'int':7,'str':'Hola','bool':True,'float':3.5,'int':2} # Tratar de no respetir tipos de caracteres porque se escriben
diccionario = {10:7,20:(1,2,3),'lista':['Control','python']}        
cerdo = {
            'Corte':['1) Tocino','2) Barriga','3) Lomo','4) Chuleta','5) Pierna','6) Pesuña'],
            'Cantidad':[100,9,11,35,6,18],
            'Valor':[1.7,9.8,10.9,4.4,12,3.2]
        }
datos= dicc = {'nombre':'sergio','edad':25}
datos
datos['genero']='m'              # Agrego datos a Diccionario
del datos['edad']                # Quito Datos de Diccionario

datos.values()      #dict_values(['sergio', 'm'])    Valores
datos.keys()        #dict_keys(['nombre', 'genero']) Llaves
datos.items()       # Recupero ambos
datos=datos.copy()  #Devuelve copia dicionaio original
datos.clear         #Borra el diccionario

dicc2=dicc.fromkeys   
a=cerdo.get('Cantidad'[0])      # Devuelve el Valor del Key 

dicc.setdefault     # Agrega Keys al diccionario

a= 222222
print(a.isnumeric())

tienda = {
         'Item':['Lapiz','Carpeta','Marcador'],
         'Cantidad':[3,20,5],
         'Valor':[3.5,4.25,7.85]
         }
print(tienda)


dicc2={'x':6.2,'p':-8,'v':6}
dicc.update(dicc2)          # Actualiza y Agrega nuevas Keys


print(a)