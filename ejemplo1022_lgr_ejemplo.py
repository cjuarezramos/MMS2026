import numpy as np
import matplotlib.pyplot as plt
import control as ct

G = ct.tf([1],[1,3,2,0])

ct.root_locus_plot(G)
plt.show()