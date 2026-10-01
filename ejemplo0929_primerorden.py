import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R = 100.0
C = 0.06

def primer_orden(t, x):
    dxdt = -1/(R * C)*x
    return dxdt

# Condiciones iniciales
x0 = [100.0]  # Valor inicial de x

# Tiempo de simulación
tsim= 30
t_span = (0, tsim)
t_eval = np.linspace(0, tsim, 1000)

# Resolver la EDO
sol = solve_ivp(primer_orden, t_span, x0, t_eval=t_eval)

# Graficar el resultado
plt.plot(sol.t, sol.y[0])
plt.xlabel('Tiempo')
plt.ylabel('x')
plt.title('Respuesta del sistema de primer orden')
plt.grid(True)
plt.show()
