from tkinter import *
from tkinter.ttk import *


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
