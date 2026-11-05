# codigo para explicar lugar de las raìces

# librerias
import numpy as np
import matplotlib.pyplot as plt
import control as ct
#· datos s del motor
R  = 6 #Ω
L  = 3 #mH
Ka = 0.02 #V·s/rad
Km = 0.02 #N·m/A
B  = 5e-5 #N·m·s/rad
J  = 1e-5 #kg·m²
# Funcion ejemplo
# G0 = motor DC  w/V
num0 = Ka
den0 = [J*L,L*B+J*R,Ka*Km]
G0 = ct.tf(num0,den0)
sol0_la = ct.step_response(G0)
plt.plot(sol0_la.t,sol0_la.y[0][0])
print(G0.poles())
polos = G0.poles()
Z = - np.real(polos[0])/np.abs(polos[0])
print(Z)
plt.show()

# Funcion de transferencia de lazo cerrado W/Wref
k = 0.1
G0_lc = ct.feedback(k*G0,1)
print(G0_lc)
polos = G0_lc.poles()
print(polos)
Z = - np.real(polos[0])/np.abs(polos[0])
print(Z)

sol0_lc = ct.step_response(G0_lc)
plt.plot(sol0_lc.t,sol0_lc.y[0][0])
plt.show()