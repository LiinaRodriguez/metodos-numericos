from texttable import Texttable
from sympy import symbols, sympify
import math

def interpolacionLineal(funcion_expresion, xl, xu, tolerancia, Flag):

    x = symbols('x')
    #funcion_expresion = sympify(funcion)
    print("Expresion simbolica:", funcion_expresion)
    i = 0
    resultado = []
   
    ea = float("inf")
    xr = 0
    resultado.append(["Iteracion", "xl", "f(xl)", "xu", "f(xu)", "xr", "Ea"])

    max_iter = 30
    if Flag == False:

        while ea > tolerancia and i < max_iter:
            i += 1  
            xr_anterior = xr
            f_xl = funcion_expresion.subs(x, xl)
            f_xr = funcion_expresion.subs(x, xr)
            f_xu = funcion_expresion.subs(x, xu)
            xr = xu - ((f_xu)*(xl - xu))/(f_xl - f_xu)
            ea = abs(((xr - xr_anterior) / xr) * 100)
            resultado.append([i, round(xl,4), round(f_xl,4), round(xu, 4), round(f_xr, 4), round(xr, 4), round(ea,4)])

            criterio_signo = f_xl * f_xr
            if criterio_signo < 0:
                 xu = xr
            elif criterio_signo > 0:
                 xl = xr
        return resultado
    
    elif Flag == True:
       
        iteraciones = tolerancia
        for j in range(iteraciones):
            xr_anterior = xr
            f_xl = funcion_expresion.subs(x, xl)
            f_xr = funcion_expresion.subs(x, xr)
            f_xu = funcion_expresion.subs(x, xu)
            xr = xu - ((f_xu)*(xl - xu))/(f_xl - f_xu)
            ea = abs(((xr - xr_anterior) / xr) * 100)
            resultado.append([j, round(xl,4), round(f_xl,4), round(xu, 4), round(f_xr, 4), round(xr, 4), round(ea,4)])

            criterio_signo = f_xl * f_xr
            if criterio_signo < 0:
                 xu = xr
            elif criterio_signo > 0:
                 xl = xr
        return resultado

def dataInput(funcion_entry, xl_entry, xu_entry, tolerancia_entry, criterio):
        #preparar los datos
        funcion_str = str(funcion_entry.get())
        funcion_expresion = process_function_input(funcion_str)
        

        xl = float(xl_entry.get())
        xu = float(xu_entry.get())
        Tolerancia = int(tolerancia_entry.get())
        Flag = bool(criterio.get())

        Data = interpolacionLineal(funcion_expresion, xl, xu, Tolerancia, Flag)
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
