from tkinter import StringVar, Tk
from tkinter.ttk import *

from models.calculator_model import CalculatorModel
import tkinter as tk


class CalculatorView(Tk):
  def __init__(self) -> None:
    super().__init__()

    self.title("Calculadora")

    self.inputsFrame = InputsFrame(self)
    self.inputsFrame.pack()
    
    ButtonsFrame(self, self.click).pack()

  def click(self, value: str) -> None:
      model = CalculatorModel()
      if value == "=": 
          expression = self.inputsFrame.get_input("infix")

          posfix = model.infix2posfix(expression)

          value = model.posfix2value(posfix)

          self.inputsFrame.update_input("value", value)
          self.inputsFrame.update_input("posfix", posfix)
            
      elif value == "AC":
          self.inputsFrame.update_input("infix", "")
      elif value ==  "DEL":
          last = self.inputsFrame.get_input("infix", value[-1])
          self.inputsFrame.update_input("infix", last )
      else:
        self.inputsFrame.update_input("infix", self.inputsFrame.get_input("infix") + value + " ")


class InputsFrame(Frame):
  def __init__(self, master) -> None:
    super().__init__(master)

    self.vars: dict[str, StringVar] = {
      'infix': StringVar(),
      'posfix': StringVar(),
      'value': StringVar()
    }

    self._create_input_row("Infix: ", self.vars['infix'], 0)
    self._create_input_row("Postfix: ", self.vars['posfix'], 1)
    self._create_input_row("Resultado: ", self.vars['value'], 2)


  def _create_input_row(self, label_text: str, text_var: StringVar, row: int):
    Label(self, text=label_text, font=("Arial", 14)).grid(row=row, column=0, pady=2)
    Entry(self, font=("Arial", 14), textvariable=text_var).grid(row=row, column=1, pady=2)

  
  def update_input(self, input_name: str, value: str) -> None:
    self.vars[input_name].set(value)


  def get_input(self, input_name: str) -> str:
    return self.vars[input_name].get()


class ButtonsFrame(Frame):
  def __init__(self, master, clickFn) -> None:
    super().__init__(master)


    buttons: list[tuple[str, str, str, str, str]] = [
      ( "√"  , "EXP", "log" , "ln"  , "sin"  ),
      ( "cos", "tan", "asin", "acos", "atan" ),
      ( "sec", "csc", "cot" , "("   , ")"    ),
      ( "7"  , "8"  , "9"   , "AC"  , "DEL"  ),
      ( "4"  , "5"  , "6"   , "x"   , "/"    ),
      ( "1"  , "2"  , "3"   , "+"   , "-"    ),
      ( "0"  , '.'  , 'π'   , "%"   , "="    ),
    ]

    for i, row in enumerate(buttons):
      for j, value in enumerate(row):
        Button(self, text=value,  command=lambda val=value: clickFn(val)).grid(row=i, column=j, ipady=8)  
