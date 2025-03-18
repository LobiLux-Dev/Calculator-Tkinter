from view.calculator_view import CalculatorView
from models.calculator_model import CalculatorModel

class CalculatorController:
  def __init__(self):
    self.model = CalculatorModel()
    self.view = CalculatorView(self)

  
  def click(self, value: str):
    set = self.view.inputsFrame.update_input
    get = self.view.inputsFrame.get_input

    set("posfix", "")
    set("value", "")

    match value:
      case '10ˣ':
        set("infix", get("infix") + '10 ^ ( ')
      case 'e':
        set("infix", get("infix") + 'e ^ ( ')
      case 'x':
        set("infix", get("infix") + ' * ')
      case 'AC':
        set("infix", "")
      case 'DEL':
        if (val := get('infix').split()).pop():
          if val and val[-1].isalpha():
            val.pop()

          set('infix', " ".join(val) + " ")
      case '=':
        posfix = self.model.infix2posfix(get("infix"))
        set("posfix", posfix)
        value = self.model.posfix2value(posfix)
        set("value", value)
      case _ if value.isnumeric() or value in ['.', 'π', '%']:
        set("infix", get("infix") + value)
      case _ if value.isalpha():
        set("infix", get("infix") + value + ' ( ')
      case _:
        current_infix = get("infix")
        set("infix", current_infix + ' ' + value + ' ')


  def run(self):
    self.view.mainloop()
