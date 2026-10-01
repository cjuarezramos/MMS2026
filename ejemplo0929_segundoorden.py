import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

M = 0.5  # Masa del objeto (kg)
K = 100.0  # Constante del resorte (N/m)
B = np.sqrt(4 * K * M) * 2 # Coeficiente de amortiguamiento (N·s/m)
def F(t):
    return 1

def segundo_orden(t, y):
    x,v = y
    dydt = [v, -K/M * x - B/M * v + F(t)/M]
    return dydt

# Condiciones iniciales
x0 = 0.1  # Posición inicial (m)
v0 = 0.0  # Velocidad inicial (m/s)

# Tiempo de simulación
discriminante = (B/(2*M))**2 - K/M
if discriminante > 0:
    s1 = -B/(2*M) + np.sqrt(discriminante)
    s2 = -B/(2*M) - np.sqrt(discriminante)
elif discriminante == 0:
    s1 = s2 = -B/(2*M)
else:
    s1 = -B/(2*M) + 1j * np.sqrt(-discriminante)
    s2 = -B/(2*M) - 1j * np.sqrt(-discriminante)
print(f"Polos del sistema: s1 = {s1}, s2 = {s2}")
tsim = 1.25
h = 0.01
t_eval = np.arange(0, tsim, h)
# Resolver la EDO
sol = solve_ivp(segundo_orden, (0, tsim), [x0, v0], t_eval=t_eval)
plt.figure()
plt.plot(sol.t, sol.y[0])
plt.title('Respuesta del sistema de segundo orden')
plt.xlabel('Tiempo [s]')
plt.ylabel('Posición [m]')
plt.grid(True)
plt.show()

