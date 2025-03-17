from tkinter import StringVar, Tk
from tkinter.ttk import *

class CalculatorView(Tk):
  def __init__(self, controller) -> None:
    super().__init__()
    self.controller = controller

    self.title("Calculadora")

    self.inputsFrame = InputsFrame(self)
    self.inputsFrame.pack()
    
    ButtonsFrame(self, controller).pack()


class InputsFrame(Frame):
  def __init__(self, master):
    super().__init__(master)

    self.vars: dict[str, StringVar] = {
      'infix': StringVar(),
      'posfix': StringVar(),
      'value': StringVar()
    }

    self._create_input_row("Infix: ", self.vars['infix'], 0)
    self._create_input_row("Postfix: ", self.vars['posfix'], 1)
    self._create_input_row("Resultado: ", self.vars['value'], 2)


  def _create_input_row(self, label_text: str, text_var: StringVar, row: int) -> None:
    Label(self, text=label_text, font=("Arial", 14)).grid(row=row, column=0, pady=2)
    Entry(self, font=("Arial", 14), textvariable=text_var).grid(row=row, column=1, pady=2)

  
  def update_input(self, input_name: str, value: str) -> None:
    self.vars[input_name].set(value)


  def get_input(self, input_name: str) -> str:
    return self.vars[input_name].get()


class ButtonsFrame(Frame):
  def __init__(self, master, controller) -> None:
    super().__init__(master)
    self.controller = controller

    buttons: list[tuple[str, str, str, str, str]] = [
      ( "sin" , "cos" , "tan"  , "log" , "ln"   ),
      ( "asin", "acos", "atan" , "EXP" , "10ˣ"  ),
      ( "sec" , "csc" , "cot"  , "("   , ")"    ),
      ( "7"   , "8"   , "9"    , "AC"  , "DEL"  ),
      ( "4"   , "5"   , "6"    , "√"   , "^"    ),
      ( "1"   , "2"   , "3"    , "x"   , "/"    ),
      ( "0"   , '.'   , "="    , "+"   , "-"    ),
    ]

    for i, row in enumerate(buttons):
      for j, value in enumerate(row):
        Button(self, text=value, command=lambda val=value: self.controller.click(val)).grid(row=i, column=j, ipady=8)  
