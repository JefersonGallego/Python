cerdo = {
            'Corte':['1) Tocino','2) Barriga','3) Lomo','4) Chuleta','5) Pierna','6) Pesuña'],
            'Cantidad':[100,9,11,35,6,18],
            'Valor':[1.7,9.8,10.9,4.4,12,3.2]
        }
pollo = {
            'Corte':['1) Pechuga','2) Rabadilla','3) Muslos','4) Patas'],
            'Cantidad':[10,2,20,15],
            'Valor':[6.5,4.1,4.6,2.4]
        }
res =   {
            'Corte':['1) Paleta','2) Costilla','3) Lomo','4) Pierna','5) Pecho'],
            'Cantidad':[3,8,5,4,3],
            'Valor':[4.5,8.14,7.45,15.4,6.8]
        }
# Diccionario Principal
carniceria = dict(Res=res,Pollo=pollo,Cerdo=cerdo)   # Ingreso cerdo,pollo,res en Craniceria
total=0                                              # Contador para el total a pagar

def mostrar(x):   # Funcion para mostrar inventario

     for j in x:        # Busco j en Carniceria  
        print('-'*20,j,'-'*20)     
        for fila in zip(*([k]+(v) for k,v in x[j].items())):   # Imprimo Keys y Values Tabla
            print(f'{fila[0]:<13}',f'{fila[1]:>15}',f'{fila[2]:>25}')

def mostrar_1(x):   # Funcion para mostrar inventario de Compras
            for fila in zip(*([k]+(v) for k,v in x.items())):   # Imprimo Keys y Values Tabla
                print(f'{fila[0]:<13}',f'{fila[1]:>15}',f'{fila[2]:>25}')

def comprar(): # funcion para solicitar la cantidad que deseo llevar 
    cantidad=int(input('Que Cantidad desea llevar: ')) 

def resta_inventario(cant,key,pos):
    global total
    p=int(pos-1)
    w=int(carniceria[key]['Cantidad'][p])     # Cantidada del corte
    y=float(carniceria[key]['Valor'][p])      # Valor del Corte
    resta=w-cant
    if resta>=0:
        carniceria[key]['Cantidad'][p]=resta
        print('Fueron vendidas: ',cant, ' Unidades')
        subtotal=y*cant
        print(f'El subtotal es : {subtotal}')
        total=total+subtotal
        print(f'El valor total es : {total}')
        
        
    else: 
        print(f'No se puede hacer la venta ya que la cantidad requerida no esta disponible\nDisponible en inventario {w}')

def ingreso_corte(corte,animal,tipo):
            print(corte)
            cantidad=int(input('Que Cantidad desea llevar: ')) 
            resta_inventario(cantidad,animal,tipo)

            
Flag1=True      # Bandera While Principal
Flag2=False     # Bandera While Secundario (Sub-menu "Compras")


while Flag1:     # Bandera Principal


    print('\n\n\t\tBienvenidos a la Carniceria LOS MARADONIANOS\n\n\t1.Comprar\n\t2.Inventario\n\t3.Total\n\t4.Salir\n\n')    
    
    OP=int(input(f'Elija una opcion entre 1 y 4: '))   # Elija Opcion

    if OP>=1 and OP<=4:
      Flag2=True  
      while Flag2 :
        if OP==1:
            print('\n\nComprar')
            print('\n\n\t\t¿Que tipo de Carne desea comprar: \n\n\t1.Res\n\t2.Cerdo\n\t3.Pollo\n\t4.Salir\n\n')
            tipo=int(input(f'Elija una Opcion: ')) 

            if tipo>=1 and tipo<=4:    # Que tipo de Carne
                 if tipo==1:
                     print('RES')      # Carne de RES
                     mostrar_1(res)
                     tipo_1=int(input(f'Elija una Opcion: '))

                     if tipo_1>=1 and tipo_1<=5: # Que tipo de Carne de Res?
                         if tipo_1==1:
                             ingreso_corte('Paleta','Res',tipo_1)
                                                                                                                  
                         elif tipo_1==2:
                             ingreso_corte('Costilla','Res',tipo_1)
                             
                         elif tipo_1==3:
                             ingreso_corte('Lomo','Res',tipo_1)

                         elif tipo_1==4:
                             ingreso_corte('Pierna','Res',tipo_1)
                            
                         elif tipo_1==5:
                             ingreso_corte('Pecho','Res',tipo_1)
                             
                 elif tipo==2:        
                     print('CERDO')    # Carne de Cerdo
                     mostrar_1(cerdo)
                     tipo_2=int(input(f'Elija una Opcion: ')) 

                     if tipo_2>=1 and tipo_2<=6: # Que tipo de Carne de Cerdo?
                         if tipo_2==1:
                             ingreso_corte('Tocino','Cerdo',tipo_2)
                            

                         elif tipo_2==2:
                             ingreso_corte('Barriga','Cerdo',tipo_2)
                             

                         elif tipo_2==3:
                             ingreso_corte('Lomo','Cerdo',tipo_2)
                             

                         elif tipo_2==4:
                             ingreso_corte('Chuleta','Cerdo',tipo_2)
                             

                         elif tipo_2==5:
                             ingreso_corte('Pierna','Cerdo',tipo_2)
                             

                         elif tipo_2==6:
                             ingreso_corte('Pesuña','Cerdo',tipo_2)
                            


                 elif tipo==3:
                     print('POLLO')   # Carne de Pollo
                     mostrar_1(pollo)
                     tipo_3=int(input(f'Elija una Opcion: ')) 

                     if tipo_3>=1 and tipo_3<=6: # Que tipo de Carne de Cerdo?
                         if tipo_3==1:
                             ingreso_corte('Pechuga','Pollo',tipo_3)
                             

                         elif tipo_3==2:
                             ingreso_corte('Rabadilla','Pollo',tipo_3)
                             

                         elif tipo_3==3:
                             ingreso_corte('Muslos','Pollo',tipo_3)
                             
                         elif tipo_3==4:
                             ingreso_corte('Patas','Pollo',tipo_3)
                             
                         

                 elif tipo==4:    # Salir Sub-Menu Compras
                    print('salir')
                    break
                     
            else:
                print('Opcion no valida; debe ser entre 1 y 4')

        elif OP==2:
            print('\t\tInventario')
            mostrar(carniceria)     
            Flag2=False
            
        elif OP==3:

            print('-'*40 ,f'\nEl total gastado es : ${total}\n','-'*40) 


            Flag2=False
        elif OP==4:
            print('\n\n\n***Gracias por su Preferencia*\n\n\n' )
            Flag2=False
            Flag1=False
            
 
    else:
        print('Opcion no valida; debe ser entre 1 y 4')