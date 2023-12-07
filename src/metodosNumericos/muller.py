from texttable import Texttable
from sympy import symbols, sympify
import math


def muller(funcion_expresion, x0, x1, x2, tolerancia, Flag):
    x = symbols('x')
    #funcion_expresion = sympify(funcion)
    i = 0
    resultado = []
   
    ea = float("inf")
    resultado.append(["Iteracion", "x1",  "x2", "x3", "xr", "Ea"])

    max_iter = 30

    if Flag == False:
         while ea > tolerancia and i < max_iter:
              f0 = funcion_expresion.subs(x, x0)
              f1 = funcion_expresion.subs(x, x1)
              f2 = funcion_expresion.subs(x, x2)

              h0 = x1 - x0
              h1 = x2 - x1

              d0 = (f1 - f0) / (x1 - x0)
              d1 = (f2 - f1) / (x2 - x1)

              a = (d1 - d0) / (h1 + h0)
              b = (a*h1 + d1)
              c = f2

              x31 = (x2 - (2*c)/(b + math.sqrt(b**2 - 4*a*c)))
              x32 = (x2 - (2*c)/(b - math.sqrt(b**2 - 4*a*c)))
    
              if x31 > x32:
                x3 = (x31) 
              else:
                x3 = (x32)
              ea = abs(((x3 - x2)/ x3) * 100)
              resultado.append([i, round(x0,4), round(x1,4), round(x2,4), round(x3,4), round(ea,4)])
              i += 1
              x0 = x1
              x1 = x2
              x2 = x3
         return resultado
    elif Flag == True:
        iteraciones = tolerancia
        for j in range (iteraciones):
              f0 = funcion_expresion.subs(x, x0)
              f1 = funcion_expresion.subs(x, x1)
              f2 = funcion_expresion.subs(x, x2)

              h0 = x1 - x0
              h1 = x2 - x1

              d0 = (f1 - f0) / (x1 - x0)
              d1 = (f2 - f1) / (x2 - x1)

              a = (d1 - d0) / (h1 + h0)
              b = (a*h1 + d1)
              c = f2

              x31 = (x2 - (2*c)/(b + math.sqrt(b**2 - 4*a*c)))
              x32 = (x2 - (2*c)/(b - math.sqrt(b**2 - 4*a*c)))
    
              if x31 > x32:
                x3 = (x31) 
              else:
                x3 = (x32)
              ea = abs(((x3 - x2)/ x3) * 100)
              resultado.append([i, round(x0,4), round(x1,4), round(x2,4), round(x3,4), round(ea,4)])
              i += 1
              x0 = x1
              x1 = x2
              x2 = x3
    return resultado


def dataInput(funcion_entry, x1_entry, x2_entry, x3_entry, tolerancia_entry, criterio):
        #preparar los datos
        funcion_str = str(funcion_entry.get())
        funcion_expresion = process_function_input(funcion_str)

        x1 = float(x1_entry.get())
        x2 = float(x2_entry.get())
        x3 = float(x3_entry.get())
        Tolerancia = int(tolerancia_entry.get())
        Flag = bool(criterio.get())

        Data = muller(funcion_expresion, x1, x2, x3, Tolerancia, Flag)
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
