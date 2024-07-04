# XOR  --------  RED MULTICAPA

import numpy as np
def hardlim(v):
    if v < 0:
        return 0.0
    else:
        return 1.0

X_ih = np.array([[1, 0, 0],    # P0
                 [1, 0, 1],    # P1
                 [1, 1, 0],    # P2
                 [1, 1, 1]])   # P3

W_ih = np.array([[-1.5, 1.0, 1.0],    # N1
                 [-0.5, 1.0, 1.0]])   # N2

v1 = np.dot(X_ih,W_ih[0])     
v2 = np.dot(X_ih,W_ih[1])

out1 = np.array([]) 
out2 = np.array([]) 

for i,j in enumerate(v1):
    out1=np.append(out1,hardlim(v1[i]))
    out2=np.append(out2,hardlim(v2[i]))

X_ho = np.stack((np.ones(len(out1)),out1,out2),axis=1)
W_ho= np.array([-0.5,-1,1])
v3 = np.dot(X_ho,W_ho)

y = np.array([]) 
for i in range(len(v3)):
    y=np.append(y,hardlim(v3[i]))

print(v1,v2,v3,y)





