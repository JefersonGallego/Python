# Verificacion de T_Clab
import tclab_cae as tclab
import time

lab=tclab.TCLab_CAE()  

print('Turn On the heaters for 5000 seconds')
lab.Q1(50) # Porcentaje 0-100%
lab.LED(100)

for i in range(5001):
    print('Time:', i, 'T1:', lab.T1, 'T2:', lab.T2,'T3:', lab.T3, 'I1:',lab.I1)
    time.sleep(1)

lab.Q1(0)
lab.LED(0)
lab.close()