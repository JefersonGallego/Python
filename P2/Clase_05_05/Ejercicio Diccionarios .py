materias = {
            'Instrumentacion':[],
            'Control':[],
            'Programacions':[]
            }

for key in materias:
    print('='*5, key, '='*5)     # ateriscos 
    for i in range(1,4):
        materias[key].append(float(input(f'Nota  {i}: ')))     # agregar cosas a un diccionario

    print('Las notas Medias del las Materias')

    for key, value in materias.items():
        print(key, '=' , sum(value)/3)


print('\n\n\t\tBienvenidos a la Carniceria LOS MARADONIANOS\n\n\t1.Comprar\n\t2.Inventario\n\t3.Total\n\t4.Salir\n\n')    
        
        