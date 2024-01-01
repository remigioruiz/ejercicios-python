import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp
from math import pi
import pylab as pl
from math import log10

plt.close('all')

Vm= float(input("Amplitud de la Moduladora: "))
Fm= float(input("Frecuancia de la Moduladora: "))
Vc= float(input("Amplitud de la Portadora: "))
Fc= float(input("Frecuencia de la Portadora: "))
kf= float(input("Factor de sensibilidad de frecuencia: "))
n= float(input("Numero de periodos: "))
print("")

z = 50
Af = kf*Vm
B = Af/Fm

Fs = 50000 # Frecuencia de muestreo
x = 0
n0 = [] 
bessel = []
f = np.arange(0,10,1)

# ECUACIONES PARA HALLAR BESSEL
for i in range(0,len(f)):
    x = round(sp.jv(i,B),2)
    bessel.append(x)

n_positivos = bessel[1:11];
n_negativos = np.flip(n_positivos);
n0.append(bessel[0]);

jn = np.concatenate((n_negativos,n0,n_positivos))

nB = 4
Bwb = 2*Fm*nB
BWc = 2*(Af*Vm)


f_ns = []
f_ps = []
F0 = []
F0.append(Fc)

for f_inicial in range(0,len(f)):

    if f_inicial == 0:
        f_1=Fc-Fm;
        f_inicial=f_1;

    else:
        f_1 = f_1-Fm;
        f_inicial=f_1;

    f_ns.append(f_inicial);