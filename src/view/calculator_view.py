from tkinter import StringVar, Tk
from tkinter.ttk import *

class CalculatorView(Tk):
  def __init__(self, controller):
    super().__init__()
    self.controller = controller

    self.title("Calculadora")

    self.inputsFrame = InputsFrame(self, controller)
    self.inputsFrame.pack()
    
    ButtonsFrame(self, controller).pack()

    # self.configure(padx=8)

    # self.model = CalculatorModel()

    # infixStr = tk.StringVar()
    # posfixStr = tk.StringVar()
    # valueStr = tk.StringVar()
    
    # infixInput = tk.Entry(self, font=("Arial", 14), textvariable=infixStr, width=30, bd=5,insertwidth=3, bg="powder blue",justify="left")
    # infixInput.grid(row=0, column=0)
    # Label(self, text=":Infix", font=("Arial", 14)).grid(row=0, column=1)

    # buttonsContainer = Frame(self, padding=(0, 10))
    # buttonsContainer.grid(columnspan=2)


    # def click(value: str):
    #   posfixStr.set("")
    #   valueStr.set("")

    #   match value:
    #     case "AC":
    #       infixStr.set("")
    #     case "DEL":
    #       if (val := infixStr.get().split()):
    #         val.pop()

    #         if val and val[-1].isalpha():
    #           val.pop()

    #         infixStr.set(" ".join(val))
    #     case "=":
    #       print(f"{infixStr.get()}asdasd")
    #       posfix = self.model.infix2posfix(infixStr.get())


    #       valueStr.set(self.model.posfix2value(posfix))
    #     case _:
    #       if not (value.isnumeric() or value == "." or value == ")") and (val := infixStr.get().split()) and val[-1].isnumeric():
    #         infixStr.set(infixStr.get() + " " + value)
    #       else:
    #         infixStr.set(infixStr.get() + value)


    # buttons: list[tuple[str, str, str, str, str]] = [
    #   ( "√"  , "EXP", "log" , "ln"  , "sin"  ),
    #   ( "cos", "tan", "asin", "acos", "atan" ),
    #   ( "sec", "csc", "cot" , "("   , ")"    ),
    #   ( "7"  , "8"  , "9"   , "AC"  , "DEL"  ),
    #   ( "4"  , "5"  , "6"   , "x"   , "/"    ),
    #   ( "1"  , "2"  , "3"   , "+"   , "-"    ),
    #   ( "0"  , '.'  , 'π'   , "%"   , "="    ),
    # ]

    # values: dict[str, str] = {
    #   "√": "sqrt ( ",
    #   "EXP": "alog ( ",
    #   "log": "log ( ",
    #   "ln": "ln ( ",
    #   "sin": "sin ( ",
    #   "cos": "cos ( ",
    #   "tan": "tan ( ",
    #   "asin": "asin ( ",
    #   "acos": "acos ( ",
    #   "atan": "atan ( ",
    #   "sec": "sec ( ",
    #   "csc": "csc ( ",
    #   "cot": "cot ( ",
    #   "(": "( ",
    #   ")": ") ",
    #   "7": "7",
    #   "8": "8",
    #   "9": "9",
    #   "AC": "AC",
    #   "DEL": "DEL",
    #   "4": "4",
    #   "5": "5",
    #   "6": "6",
    #   "x": "* ",
    #   "/": "/ ",
    #   "1": "1",
    #   "2": "2",
    #   "3": "3",
    #   "+": "+ ",
    #   "-": "- ",
    #   "0": "0",
    #   '.': ".",
    #   'π': "π",
    #   "%": "%",
    #   "=": "=",
    # }
    
    # for i, row in enumerate(buttons):
    #   for j, value in enumerate(row):
    #     Button(buttonsContainer, text=value, command=lambda val=value: click(values[val]), width=8).grid(row=i, column=j, ipadx=15, ipady=8)
    
    # entrada2 = tk.Entry(self, font=("Arial", 14), textvariable=posfixStr, width=30, bd=5,insertwidth=3, bg="powder blue", justify="left")
    # entrada2.grid()
    # Label(self, text=":Postfix", font=("Arial", 14)).grid(row=2, column=1)
    # entrada3 = tk.Entry(self, font=("Arial", 14), textvariable=valueStr, width=30, bd=5,insertwidth=3, bg="powder blue", justify="left")
    # entrada3.grid()
    # Label(self, text=":Resultado", font=("Arial", 14)).grid(row=3, column=1)


class InputsFrame(Frame):
  def __init__(self, master, controller):
    super().__init__(master)
    self.controller = controller

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

  
  def update_input(self, input_name: str, value: str):
    self.vars[input_name].set(value)


  def get_input(self, input_name: str) -> str:
    return self.vars[input_name].get()


class ButtonsFrame(Frame):
  def __init__(self, master, controller):
    super().__init__(master)
    self.controller = controller

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
        Button(self, text=value, command=lambda val=value: self.controller.click(val)).grid(row=i, column=j, ipady=8)  
