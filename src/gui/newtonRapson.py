from texttable import Texttable
from sympy import symbols, diff, sympify

def newtonRaphson(funcion, x_anterior, x_actual, ea):
    x = symbols('x')
    funcion_expresion = sympify(funcion)
    derivada = diff(funcion_expresion, x)
    i = 0
    resultado = []
    resultado.append(["Iteracion", "X",  "Xi+1", "Ea"])
    while ea > 1e-6:
        x_anterior = x_actual
        x_actual = x_anterior - (funcion_expresion.subs(x, x_anterior) / derivada.subs(x, x_anterior))
        ea = abs(((x_actual - x_anterior) / x_actual) * 100)
        resultado.append([i, x_anterior, x_actual, ea])
        i += 1
    return resultado

def dataInput(funcion_entry, x_anterior_entry, x_actual_entry, tolerancia_entry):
         #preparar los datos
        funcion = funcion_entry.replace('^', '**').replace('x', '*x')
       
        xAnterior = int(x_anterior_entry)
        xActual = int(x_actual_entry)
        Tolerancia = int(tolerancia_entry)

        Data = newtonRaphson(funcion, xAnterior, xActual, Tolerancia)
        tabla = Texttable()
        tabla.add_rows(Data)

        print(tabla.draw())
# if __name__ == "__main__":
#     resultado = newtonRaphson('6*x**3 - 3*x**2 + 5*x - 5', 2, 1, 1)
#     tabla = Texttable()
#     tabla.add_rows(resultado)

#     print(tabla.draw())
