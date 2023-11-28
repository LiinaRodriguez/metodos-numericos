import math
from texttable import Texttable

def f(x):
  return math.exp(-x)

def metodo_punto_fijo():
  ea = 100
  x_actual = 0
  x_anterior = 0
  n = 0
  resultado = []
  resultado.append(["Iteracion", "X",  "Xi+1", "Ea"])

  while(ea > 1):
    x_anterior = x_actual
    x_actual = f(x_anterior)
    ea = abs(((x_actual - x_anterior) / x_actual ) * 100)
    resultado.append([ n, x_anterior, x_actual, ea])
    n += 1

  return resultado


if __name__ == "__main__":
  resultado = metodo_punto_fijo()
  tabla = Texttable()
  tabla.add_rows(resultado)

  print(tabla.draw())