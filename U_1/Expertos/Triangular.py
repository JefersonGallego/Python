import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fz
import pandas as pd

#Primera parte
U = np.arange(10,60.1,0.1)    # Universo del discruso 

U.min() 
U.max() 

M=fz.trimf(U,[30,37,45])      # Comjunto M Triangular

plt.plot(U,M)
plt.show()

# Segunda Parte
# Valor de pertenencia para 34,75 °C

TM= 34.75
MU_M= fz.interp_membership(U,M,TM)

print(MU_M)
