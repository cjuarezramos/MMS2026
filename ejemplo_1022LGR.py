import numpy as np
import matplotlib.pyplot as plt
import control as ct

G = ct.tf(1,[1,3,2,0])
print(G)
ct.root_locus(G)
plt.show()


G2 = ct.tf([1,1],[1,0,0])
print(G2)
ct.root_locus(G2)
plt.show()