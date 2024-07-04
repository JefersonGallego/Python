
print('Metros \t\t Pulgadas \t\t Pies')

for m in range(1,6):  #Simpre un Numero mas del valos que quiero Tomar
    
    Pulgadas= m*39.3701
    Pies= m*3.28084   
    print(f'{m} {round(Pulgadas,2):22} {round(Pies,2):21}')

print('Fin del Ciclo For')