import math
import matplotlib.pyplot as plt
import numpy as np

# listas
distanciaSDBS = list()
fracaoSDBS = list()
RED_SDBS = list()
distanciaTriton = list()
fracaoTriton = list()
RED_Triton = list()

# parâmetros de Hansen
etanol = (15.80, 8.80, 19.40)
SDBS = (17.80, 8.30, 5.00)
Triton = (16.7, 6.7, 9.1)
grafeno = (18.00, 9.30, 7.70, 6.50)


# cálculo SDBS
for fracao1 in np.arange(0, 1.001, 0.001):
	mediaD = (fracao1*SDBS[0]) + ((1-fracao1)*etanol[0])
	mediaP = (fracao1*SDBS[1]) + ((1-fracao1)*etanol[1])
	mediaH = (fracao1*SDBS[2]) + ((1-fracao1)*etanol[2])
	d = math.sqrt((4*((grafeno[0]-mediaD)**2)) + ((grafeno[1]-mediaP)**2) + ((grafeno[2]-mediaH)**2))
	distanciaSDBS.append(d)
	fracaoSDBS.append(fracao1)
	RED = d/grafeno[3]
	RED_SDBS.append(RED)

# gráfico
plt.plot(fracaoSDBS,distanciaSDBS)
plt.title('SDBS')
plt.xlabel('fração volumétrica')
plt.ylabel('Distância Grafeno/Fluido base')
plt.show()

menor_frac = fracaoSDBS[distanciaSDBS.index(min(distanciaSDBS))]
print(f'A menor fração de SDBS é {menor_frac}')
MM_SDBS = 348.48
densidade_SDBS = 1000
densidade_etanol = 789
mass_frac_SDBS = (menor_frac*(densidade_SDBS**2))/((menor_frac*(densidade_SDBS**2))-((menor_frac-1)*densidade_SDBS*densidade_etanol))
M = (mass_frac_SDBS * densidade_SDBS) / MM_SDBS
print(f'Portanto, a concentração de SDBS é {M} mol/L')

# Cálculo Triton X-100

# cálculo
for fracao2 in np.arange(0, 1.001, 0.001):
	mediaD = (fracao2*Triton[0]) + ((1-fracao2)*etanol[0])
	mediaP = (fracao2*Triton[1]) + ((1-fracao2)*etanol[1])
	mediaH = (fracao2*Triton[2]) + ((1-fracao2)*etanol[2])
	d = math.sqrt((4*((grafeno[0]-mediaD)**2)) + ((grafeno[1]-mediaP)**2) + ((grafeno[2]-mediaH)**2))
	distanciaTriton.append(d)
	fracaoTriton.append(fracao2)
	RED = d/grafeno[3]
	RED_Triton.append(RED)

# gráfico
plt.plot(fracaoTriton,distanciaTriton)
plt.title('Triton')
plt.xlabel('fração volumétrica')
plt.ylabel('Distância Grafeno/Fluido base')
plt.show()

menor_frac = fracaoTriton[distanciaTriton.index(min(distanciaTriton))]
print(f'A menor fração de Triton X-100 é {menor_frac}')
MM_Triton = 647
densidade_Triton = 1070
densidade_etanol = 789
mass_frac_Triton = (menor_frac*(densidade_Triton**2))/((menor_frac*(densidade_Triton**2))-((menor_frac-1)*densidade_Triton*densidade_etanol))
M = (mass_frac_Triton * densidade_Triton) / MM_Triton
print(f'Portanto, a concentração de Triton X-100 é {M} mol/L')
