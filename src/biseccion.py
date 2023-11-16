import numpy as np
import matplotlib.pyplot as plt
print("\n************ Metodo de biseccion  *******\n")

def f(x):
    return x**10 - 1

Xr = 0
Xl = 0
Xu = 1.3
Xr_nuevo = 0
Xr_anterior = 0
toleranciaporcentual = 1
xr_puntos = []


print(f"{12 * ' '}\t{12 * ' '}\t{12 * ' '}\t{12 * ' '}\t{12 * ' '}\t{12 * ' '}")
print("%12s \t %12s \t %12s \t %12s \t %12s \t %12s" % ("Valor Xl", "Valor Xu", "Valor Xr", "Nuevo_Xr", "Resultado", "ϵₐ %"))

for i in range(21):
    Xr_anterior = Xr
    Xr = (Xl + Xu) / 2
    Xr_nuevo = Xr
    xr_puntos.append(Xr)
    f_xl = f(Xl)
    f_xr = f(Xr)
    resultado = f_xl * f_xr

    if resultado < 0:
        Xu = Xr
    elif resultado > 0:
        Xl = Xr
    ea = abs((Xr_nuevo - Xr_anterior) / Xr_nuevo) * 100
    print("%12.8g \t %12.8g \t %12.8g \t %12.8g \t %12.3g \t %12.3g" % (Xl, Xu, Xr, Xr_nuevo, resultado, ea))

    if ea <= toleranciaporcentual:
        break

plt.plot(xr_puntos,np.zeros(len(xr_puntos)),'r+')

