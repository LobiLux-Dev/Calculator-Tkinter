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
    
    ButtonsFrame(self).pack()


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
  
  
  
  def button_click(self,value):
      self.infi = CalculatorModel()
      if value == "=": 
          expression = self.get_input("infix")
          posf = self.infi.infix2posfix(expression)
          result = self.infi.posfix2value(expression)
          self.update_input("value", str(result))
          self.update_input("posfix", str(posf))
            
      elif value == "AC":
          self.update_input(input_name="infix", value="")
      else:
        self.update_input(input_name="infix", value=self.get_input(input_name="infix") + value)

class ButtonsFrame(Frame):
  def __init__(self, master) -> None:
    super().__init__(master)
    
    calcu= InputsFrame(self)


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
        Button(self, text=value,  command=lambda v=value: calcu.button_click(v)).grid(row=i, column=j, ipady=8)  
