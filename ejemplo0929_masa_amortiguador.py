import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

M = 5
B = 0.06
def F(t):
    return np.cos(2*np.pi*t*0.01)
def masa_amortiguador(t, x):
    dxdt = 1/M * (F(t) - B*x[0])
    return [dxdt]
tsim= 420*2
t_span = (0, tsim)
t_eval = np.linspace(0, tsim, 1000)
velocidad_inicial = 0
sol = solve_ivp(masa_amortiguador, t_span, [velocidad_inicial], t_eval=t_eval)
plt.plot(sol.t, sol.y[0])   
plt.xlabel('Tiempo [s]')
plt.ylabel('Velocidad [m/s]')
plt.title('Masa-Amortiguador')
plt.grid(True)
plt.show()