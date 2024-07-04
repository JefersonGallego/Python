## Examen parcial - programacion 2



def Ingreso_nombres():
    nombres=[]
    flag=True
    while flag:
        cant_habitantes = input('Ingrese el numero de habitantes del apartamento : ')
        if cant_habitantes.isnumeric():
            cant_habitantes= int(cant_habitantes)
            for i in  range(0,cant_habitantes):
                nombres.append(input(f'Ingrese el nombre del usuairo {i+1} : '))
            flag=False
            return nombres
        else:
            print('El dato digitado no es numerico, por favor ingresar un dato numerico')


def Ingreso_dias(name):
    dias=[]   
    flag=True
    j=0
    while flag:
        h=input(f'Ingrese la cantidad de dias vividos del inquilino {name[j]} : ')
        if h.isnumeric() :
            h=int(h)
            if h<=30 and h>0:
                dias.append(h)
                j+=1
            else :
                print('El dato Ingresado no es valido,debe de ser mayor o igual 1 y  menor o igual a 30, por favor digite un dato dentro de este rango')

            if len(name)==len(dias):
                flag=False                
        else :
            print('El dato no es numerico, por favor ingrese un dato numerico')
    return dias

def imprimir_datos(a,b):
    for i in range(0,len(a)):

        print(f'El inquilino {a[i]} vivio un total de {b[i]} en la vivienda ')

def acum_dias (dias):
    y=0
    for i in range(0,len(dias)):
        y = int(dias[i])+y
    return y
    
def calcular_pago(dias,valor_luz,acum,valor_arriendo):
    pagos=[]
    for i in range(0,len(dias)):
        a=int(dias[i])
        au=(a/(a+(acum-a)))
        pagos.append(float((au*valor_luz)+(valor_arriendo/len(dias))))
    return pagos

def validar_Dato(frase):
    while True:
            valor= input(frase)     
            if valor.isnumeric():
                valor = int(valor)
                break
            else:
                print('El dato ingresado no es numerico , por favor ingresar un dato numerico')

    return valor

def limites(frase,minimo,maximo):
    
    flag=True
    while flag:
        y=validar_Dato(frase)
        if y<=maximo and y>=minimo:
            flag=False
        else:
            print(f'El dato ingresado esta por fuera de los limites establecidos min {minimo} y max {maximo}')

    return y

def mostrar_fact(nombre,pago,dias):
    for i in range(len(nombre)):
        print(f'{nombre[i]}\t\t {round(pago[i],2)}\t\t{dias[i]}')

def mostrar_pant(nombre,pago,luz,arriendo,consumo):
    for i in range(len(nombre)):
        print(f'{nombre[i]}\t =\t {round(pago[i],2)}')
    print(f'La potencia consumida fue {luz/consumo}\nTotal a pagar : {luz+arriendo}')



    
"""
if __name__ =='__name__':

    a=Ingreso_nombres()
    b=Ingreso_dias(a)
    arriendo = validar_Dato('Por favor ingresar el valor del arriendo : ')
    luz = validar_Dato('Por favor ingresar el valor de la factura de luz : ')
    valor_kw=validar_Dato('Por favor ingresar el valor del kW/h: ')
    w=acum_dias(b)
    pagos=calcular_pago(b,luz,w,arriendo)
    for i in range(len(a)):
        k=pagos[i]
        print(f'El valor a pagar del inquilino {a[i]} es  :  {round(pagos[i],2)}')
"""
