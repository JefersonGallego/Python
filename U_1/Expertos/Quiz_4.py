import numpy as np
import matplotlib.pyplot as plt

v=np.array([])
y = np.array([])

def sgn(v):   # hardlims
    if v<0.0:
        return -1.0
    else:
        return 1.0

def hardlim(v):

    if v<0.0:
        return 0.0
    else:
        return 1.0
 
def percep_out(x, w):
    y = np.array([])
    for i, j in enumerate(x):
        y = np.append(y, sgn(np.dot(w, x[i])))
    return y

# Vectores
w=np.array([1.35, -0.39, -0.75]) # Vector de pesos
x=np.array([[1.0,4.0,-1.5],
            [1.0,-2.0,-2.0],
            [1.0,2.75,1.5],
            [1.0,-0.5,1.0],
            [1.0,1.0,2.5],
            [1.0,2.0,1.2]])

y = percep_out(x,w)
print(f"Salida de percepton: {y}")

# Recta Discriminante
X_2= (-1*w[0])/w[2]
X_1= (-1*w[0])/w[1]
P1=[0,X_2]
P2=[X_1,0]

# Ecuacion
xx = np.linspace(-6, 6)     # Creo tabla -3x3
yy = -(w[1]/w[2])*xx -(w[0]/w[2])   # Ecuacion de la recta

x_min, x_max = x[:, 1].min() - 2.5, x[:, 1].max() + 2.5
y_min, y_max = x[:, 2].min() - 2.5, x[:, 2].max() + 2.5
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.scatter(x[0,1], x[0,2], color='r') # salida 1
plt.scatter(x[1,1], x[1,2], color='r') # salida 1
plt.scatter(x[2,1], x[2,2], color='b') # salida -1
plt.scatter(x[3,1], x[3,2], color='r') # salida 1
plt.scatter(x[4,1], x[4,2], color='b') # salida -1
plt.scatter(x[5,1], x[5,2], color='b') # salida -1
plt.scatter(0,X_2, color='g')
plt.scatter(X_1,0, color='g')
plt.plot(xx, yy, 'g-')
plt.xlabel('Caracteristica x1')
plt.ylabel('Caracteristica x2')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()
