
from ast import Continue
from re import A
a = 0
while a < 100:
    #print(a)
    #a+=1
    a=a+1
    #if a>50:
       #break  #Romper Ciclo
    if a % 2 == 0: 
        continue  #Devuelve al Ciclo While 
    print(a,end=' ')
print('Ciclo Finalizo')