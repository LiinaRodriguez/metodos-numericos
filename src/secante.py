import numpy as np
import math
from texttable import Texttable

def f(x):
  return math.exp(-x) - x

def newtonRaphson():
  ea = 100
  x_actual = 0
  x_anterior = 0
  x_siguiente = 1
  i = 0
  resultado = []
  resultado.append(["Iteracion", "X",  "Xi-1", "Xi+1","Ea"])
  while(ea > 1):
    x_anterior = x_actual
    x_actual = x_siguiente
    x_siguiente = x_actual - (f(x_actual)*(x_anterior - x_actual) ) / (f(x_anterior) - (f(x_actual)))
    ea = abs(((x_actual - x_anterior) / x_actual ) * 100)

    resultado.append([ i, x_anterior, x_actual, x_siguiente, ea])
    i += 1

  return resultado

if __name__ == "__main__":
  resultado = newtonRaphson()
  tabla = Texttable()
  tabla.add_rows(resultado)

  print(tabla.draw())