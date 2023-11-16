from texttable import Texttable

def f(x):
  return x**3 - x - 1


def g(x):
  return 3*x**2-1

def newtonRaphson():
  ea = 100
  x_actual = 1
  x_anterior = 1
  i = 0
  resultado = []
  resultado.append(["Iteracion", "X",  "Xi+1", "Ea"])
  while(ea > 1):
    x_anterior = x_actual
    x_actual = x_anterior - (f(x_anterior) / g(x_anterior))
    ea = abs(((x_actual - x_anterior) / x_actual ) * 100)
    resultado.append([ i, x_anterior, x_actual, ea])
    i += 1
  return resultado

if __name__ == "__main__":
  resultado = newtonRaphson()
  tabla = Texttable()
  tabla.add_rows(resultado)

  print(tabla.draw())
