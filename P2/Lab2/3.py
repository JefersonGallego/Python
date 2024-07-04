import math

print('Grados \t\t Radianes')

for i in range(0,361,10):
     rad=(i*(2*math.pi))/360
     
     print(f'{i} \t\t {rad}')

print('Fin del Ciclo For')