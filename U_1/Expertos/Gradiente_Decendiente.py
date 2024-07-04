def grad_J(w1):
    return w1

def mse(w1):
    mse = 0.5 * (w1**2)
    return mse

def delta(w1, eta, k):
    import numpy as np
    w1_evol = np.array([])
    error_evol = np.array([])
    for i in range(k):
        w1 -= eta * grad_J(w1)
        w1_evol = np.append(w1_evol, w1)
        error_mse = mse(w1)
        error_evol = np.append(error_evol, error_mse)
        print ('iteración: ', i+1, ' w1 = ', w1, ' mse = ', error_mse)
    return w1_evol, error_evol

import numpy as np
w1, mse = delta(w1=10, eta=0.2, k=500)

