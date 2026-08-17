# Programa para resolver el problema del paracaidista
import numpy as np
import matplotlib.pyplot as plt

#º Definir las constantes
g = 9.81  # Aceleración debida a la gravedad (m/s²)
m = 68.1  # Masa del paracaidista (kg)
c = 12.5  # Coeficiente de arrastre (kg/s)

# parametros iniciales
v0 = 0.0  # Velocidad inicial (m/s)

# Variable computacionales
t = np.linspace(0, 60, 1000)  # Tiempo (s)
v = np.zeros(len(t))  # Vector de velocidad (m/s)
v[0] = v0  # Condición inicial

for i in range(len(t) - 1):
    # Ecuación diferencial: dv/dt = g - (c/m) * v
    # Solución analítica: v(t) = (m*g/c) * (1 - exp(-c*t/m))
    h = t[i+1] - t[i]  # Paso de tiempo
    v[i+1] = v[i] + h * (g - (c/m) * v[i])  # Método de Euler
    
# Graficar la velocidad en función del tiemp
plt.plot(t, v, 'bo')
plt.title('Velocidad del paracaidista en función del tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.grid()
plt.show()