from texttable import Texttable
from sympy import symbols, sympify

def secante(funcion_expresion, x_actual, x_siguiente, tolerancia, criterioF):
    x = symbols('x')
    #funcion_expresion = sympify(funcion)
    i = 0
    resultado = []
   
    ea = float("inf")
    resultado.append(["Iteracion", "X",  "Xi+1", "Ea"])

    max_iter = 30
    
    if criterioF == False:
        #resultado.append([i, round(x_actual,4), round(x_siguiente, 4), round(ea,4)])
        while ea > tolerancia and i < max_iter:
            i += 1
            x_anterior = x_actual
            x_actual = x_siguiente
            if (funcion_expresion.subs(x, x_anterior) - (funcion_expresion.subs(x, x_actual))) == 0:
                 print("Division por cero")
                 break
                 
            x_siguiente = x_actual - (funcion_expresion.subs(x, x_actual) * (x_anterior - x_actual))/(funcion_expresion.subs(x, x_anterior) - (funcion_expresion.subs(x, x_actual)))
            ea = abs(((x_actual - x_anterior) / x_actual) * 100)
            resultado.append([i, round(x_actual,4), round(x_siguiente, 4), round(ea,4)])
        return resultado
    
    elif criterioF == True:
        #resultado.append([i, round(x_anterior,4), round(x_actual, 4), round(ea,4)])
        iteraciones = tolerancia
        for j in range(iteraciones):
            x_anterior = x_actual
            x_actual = x_siguiente
            if (funcion_expresion.subs(x, x_anterior) - (funcion_expresion.subs(x, x_actual))) == 0:
                 print("Division por cero")
                 break
                 
            x_siguiente = x_actual - (funcion_expresion.subs(x, x_actual) * (x_anterior - x_actual))/(funcion_expresion.subs(x, x_anterior) - (funcion_expresion.subs(x, x_actual)))
            ea = abs(((x_actual - x_anterior) / x_actual) * 100)
            resultado.append([j+1, round(x_actual,4), round(x_siguiente, 4), round(ea,4)])
        return resultado

def dataInput(funcion_entry, x_anterior_entry, x_actual_entry, tolerancia_entry, criterio):
        #preparar los datos
        funcion_str = str(funcion_entry.get())
        funcion_expresion = process_function_input(funcion_str)

        xAnterior = float(x_anterior_entry.get())
        xActual = float(x_actual_entry.get())
        Tolerancia = int(tolerancia_entry.get())
        criterioF = bool(criterio.get())

        Data = secante(funcion_expresion, xAnterior, xActual, Tolerancia, criterioF)
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
