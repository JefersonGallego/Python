import numpy as np
import matplotlib.pyplot as plt


def dnewton(x,fx,n):
    #Matrix interpoladora de Newton
    A = np.zeros((n+1,n+1))
    for i in range(n+1):
         A[i,0]=fx[i]
         
    #Determinar coeficientes de Newton empleando la ecuación de
    #las diferencias divididas
    for i in range(n):
       for j in range(n-i):
         A[j,i+1]=(A[j+1,i]- A[0,i])/(x[j+i+1]-x[i])
         
    #Coeficientes desconocidos
    a=A[0,:]
    
    p=1 #Inicializa el polinomio
    yp = np.zeros((n,n+1)) #Matriz para hacer el producto polinomial
    
    for i in range(n):
       p =  np.convolve([1, -x[i]],p)
       yp[i,-i+n-1:] =  p*a[i+1]
       
   
    P = np.sum(yp, axis=0)
    print(P)
    P[-1] = P[-1]+a[0]
    return a,P


n=int(input('Orden del Polinomio: '))
x = np.arange(2,8.5,0.5)
Ts = (8-2)/(n) #Numero de puntos
xi=np.arange(2,8+Ts,Ts)

Fx = x ** 4
Fxi = xi ** 4


a,Px = dnewton(xi,Fxi,n)
print('Polinomio:')
for i in range(n+1):   
   if i!= 0 and Px[i]>=0:
      print(' + ',end='')
   if i == n:
      print(f'{Px[i]} ',end='')
   else:
      print(f'{Px[i]} x^{n-i} ',end='')

Pxi=np.polyval(Px,x)#Evalua o polinomio 
Pxin=np.polyval(Px,xi)#Evalua o polinomio

plt.figure()
plt.plot(x,Fx,'-k',x,Pxi,'--r',xi,Pxin,'or',linewidth=2)
plt.show()
