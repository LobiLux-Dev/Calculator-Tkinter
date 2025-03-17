from tkinter import *
from tkinter.ttk import *
 
import tkinter as tk
from tkinter import StringVar


class CalculatorView(Tk):
  def __init__(self):
    super().__init__()

    self.title("Calculadora")


    expression = StringVar()
    self.expressionEntry = Entry(self, textvariable=expression)
    self.expressionEntry.grid()

    buttonsContainer = Frame(self, padding=5)
    buttonsContainer.grid()

    widgets = [
      ( 'log' , 'sin' , 'cos' , 'tan' , 'ln'  ),
      ( 'alog', 'asin', 'acos', 'atan', 'aln' ),
      ( '7'   , '8'   , '9'   , '^'   , 'AC'  ),
      ( '4'   , '5'   , '6'   , '*'   , '/'   ),
      ( '1'   , '2'   , '3'   , '+'   , '-'   ),
      ( '0'   , '.'   , '('   , ')'   , '='   ),
    ]

    for i, row in enumerate(widgets):
      for j, value in enumerate(row):
        Button(buttonsContainer, text=value, width=5).grid(row=i, column=j)
        
      
    ventana=tk.Tk()
    ventana.title("Calculadora :3")
    ventana.geometry("445x550")

    #tamaño de los botones
    anch = 8
    larg = 3

    #botones 
    def click(num):
        global operador
        operador= operador+ str(num)
        a.set(operador)
        
      # funciones de las operaciones de cada boton
    def click(num):
        global operador
        operador=operador+str(num)
        a.set(operador)

    def clear():
        global operador
        operador=""
        a.set(operador)

    def operacion():
        global operador
        try:
            opera=eval(operador)
        except:
            clear()
            opera=("ERROR")
        a.set(opera)
        
    a= StringVar()
    campo1 = StringVar()
    campo2 = StringVar()
    campo3 = StringVar()
    operador=""


    botones = {
      ("√", "√", 1, 85),
      ("EXP", "**", 90, 85),
      ("log", "log10", 179, 85),
      ("ln", "log", 268, 85),
      ("sin", "sin", 357, 85),
      ("cos", "cos", 1, 143),
      ("tan", "tan", 90, 143),
      ("asin", "asin", 179, 143),
      ("acos", "acos", 268, 143),
      ("atan", "atan", 357, 143),
      ("sec", "1/cos", 1, 201),
      ("csc", "1/sin", 90, 201),
      ("cot", "1/tan", 179, 201),
      ("7", 7, 1, 259),
      ("8", 8, 90, 259),
      ("9", 9, 179, 259),
      ("AC", clear, 268, 259), #modificar pq es funcion
      ("DEL", "remove", 357, 259),
      ("4", 4, 1, 317),
      ("5", 5, 90, 317),
      ("6", 6, 179, 317),
      ("X", "*", 268, 317),
      ("/", "/", 357, 317),
      ("1", 1, 1, 375),
      ("2", 2, 90, 375),
      ("3", 3, 179, 375),
      ("+", "+", 268, 375),
      ("-", "-", 357, 375),
      ("0", 0, 1, 433),
      (".", ".", 90, 433),
      ("π", "π", 179, 433),
      ("%", "%", 268, 433),
      ("=", "=", 357, 433)
    }

    def new_button(texto, comando, x, y):
        return tk.Button(ventana, text=texto, width=anch, height=larg, command=lambda: click(comando)).place(x=x, y=y)

    for texto, comando, x, y in botones:
        new_button(texto, comando, x, y)

    entrada1 = tk.Entry(ventana, font=("Arial", 14), textvariable=campo1, width=30, bd=5,insertwidth=3, bg="powder blue",justify="left")
    entrada1.place(x=5, y=4)
    efix = tk.Label(ventana, text=":Infix", font=("Arial", 14))
    efix.place(x=350, y=5)
    entrada2 = tk.Entry(ventana, font=("Arial", 14), textvariable=campo2, width=30, bd=5,insertwidth=3, bg="powder blue", justify="left")
    entrada2.place(x=5, y=45)
    epos = tk.Label(ventana, text=":Postfix", font=("Arial", 14))
    epos.place(x=350, y=45)
    entrada3 = tk.Entry(ventana, font=("Arial", 14), textvariable=campo3, width=30, bd=5,insertwidth=3, bg="powder blue", justify="left")
    entrada3.place(x=5, y=500)
    r = tk.Label(ventana, text=":Resultado", font=("Arial", 14))
    r.place(x=346, y=500)




    ventana.mainloop()




