from view.calculator_view import CalculatorView
from models.calculator_model import CalculatorModel

class CalculatorController:
  def __init__(self):
    self.model = CalculatorModel()
    self.view = CalculatorView(self)

  
  def click(self, value: str):
    set = self.view.inputsFrame.update_input
    get = self.view.inputsFrame.get_input

    set(input_name="posfix", value="")
    set(input_name="value", value="")
  

    if value.isnumeric() or value in ['.', 'π', '%']:
      current_infix = get("infix")
      set(input_name="infix", value=current_infix + value)
    elif value == "AC":
      set(input_name="infix", value="")
    elif value == "DEL":
      if (val := get('infix').split()):
        val.pop()

        if val and val[-1].isalpha():
          val.pop()

        set(input_name='infix', value=" ".join(val) + '')
    elif value.isalpha() and not value in ['x']:
      current_infix = get("infix")
      set(input_name="infix", value=current_infix + ' ' + value + ' ( ')
    elif value == "=":
      current_infix = get("infix")

      posfix = self.model.infix2posfix(current_infix)
      set(input_name="posfix", value=posfix)
      value = self.model.posfix2value(posfix)
      set(input_name="value", value=value)
    else:
      current_infix = get("infix")
      set(input_name="infix", value=current_infix + ' ' + value + ' ')


  def run(self):
    self.view.mainloop()
