# Mostrar el Cudrado de los #s 1 al 10
#for i in range(1,11):
 #   print(i **2)

#print('Fin delCiclo For')

def remover_caracter(s, n):
    inicio = 0
    fin = len(s)
    resultado = s[inicio:n] + s[n+1:fin]
    return resultado

print(remover_caracter("casa",1))


print('[1,0,0]')