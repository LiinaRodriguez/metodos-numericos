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
ea = 100
toleranciaporcentual = 1
xr_puntos = []
print("%12s \t %12s \t %12s \t %12s  \t %12s" % ("Valor Xl", "Valor Xu", "Valor Xr",  "Resultado", "ϵₐ %"))

for i in range(30):

    f_xl = f(Xl)
    f_xu = f(Xu)
    Xr_anterior = Xr
    Xr = Xu - (f_xu * (Xl - Xu)) / (f_xl - f_xu)
    Xr_nuevo = Xr
    xr_puntos.append(Xr)
    f_xr = f(Xr)
    resultado = f_xl * f_xr

    if resultado < 0:
        Xu = Xr
    elif resultado > 0:
        Xl = Xr
    ea = abs((Xr_nuevo - Xr_anterior) / Xr_nuevo) * 100
    print("%12.8g \t %12.8g \t %12.8g \t %12.8g  \t %12.8g" % (Xl, Xu, Xr, resultado, ea))

    if ea <= toleranciaporcentual:
        break

plt.plot(xr_puntos,np.zeros(len(xr_puntos)),'b+')

plt.show()