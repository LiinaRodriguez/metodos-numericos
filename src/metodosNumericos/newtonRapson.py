from texttable import Texttable
from sympy import symbols, diff, sympify

def newtonRaphson(funcion_expresion, x_actual, tolerancia, criterioFlag):
    x = symbols('x')
    #funcion_expresion = sympify(funcion)
    derivada = diff(funcion_expresion, x)
    i = 0
    resultado = []
   
    ea = float("inf")
    resultado.append(["Iteracion", "Xi+1", "Ea"])

    max_iter = 30
    if criterioFlag == False:
        #resultado.append([i, round(x_anterior,4), round(x_actual, 4), round(ea,4)])
        while ea > tolerancia and i < max_iter:
            i += 1
            x_anterior = x_actual
            x_actual = x_anterior - (funcion_expresion.subs(x, x_anterior) / derivada.subs(x, x_anterior))
            ea = abs(((x_actual - x_anterior) / x_actual) * 100)
            resultado.append([i, round(x_actual, 4), round(ea,4)])
        return resultado
    
    elif criterioFlag == True:
        resultado.append([i, round(x_anterior,4), round(x_actual, 4), round(ea,4)])
        iteraciones = tolerancia
        for j in range(iteraciones - 1):
            x_anterior = x_actual
            x_actual = x_anterior - (funcion_expresion.subs(x, x_anterior) / derivada.subs(x, x_anterior))
            ea = abs(((x_actual - x_anterior) / x_actual) * 100)
            resultado.append([j+1, round(x_actual, 4), round(ea,4)])
        return resultado

def dataInput(funcion_entry, x_actual_entry, tolerancia_entry, criterio):
        #preparar los datos
        funcion_str = str(funcion_entry.get())
        funcion_expresion = process_function_input(funcion_str)

        xActual = float(x_actual_entry.get())
        Tolerancia = int(tolerancia_entry.get())
        criterioF = bool(criterio.get())

        Data = newtonRaphson(funcion_expresion, xActual, Tolerancia, criterioF)
        tabla = Texttable()
        tabla.add_rows(Data)

        print(tabla.draw())
        
        return Data

def process_function_input(funcion_str):
    x = symbols('x')
    try:
        funcion_expresion = sympify(funcion_str)
        return funcion_expresion
    except:
        print("Invalid function expression")
        return None
