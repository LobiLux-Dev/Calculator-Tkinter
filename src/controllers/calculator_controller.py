from view.calculator_view import CalculatorView
from models.calculator_model import CalculatorModel

class CalculatorController:
  def __init__(self):
    self.model = CalculatorModel()
    self.view = CalculatorView(self)

  
  def click(self, value: str):
    self.view.inputsFrame.update_input(input_name="posfix", value="")
    self.view.inputsFrame.update_input(input_name="value", value="")
  

    if value.isnumeric() or value in ['.', 'π', '%']:
      current_infix = self.view.inputsFrame.get_input("infix")
      self.view.inputsFrame.update_input(input_name="infix", value=current_infix + value)
    elif value == "AC":
      self.view.inputsFrame.update_input(input_name="infix", value="")
    elif value.isalpha():
      current_infix = self.view.inputsFrame.get_input("infix")
      self.view.inputsFrame.update_input(input_name="infix", value=current_infix + ' ' + value + ' ( ')
    elif value == "=":
      current_infix = self.view.inputsFrame.get_input("infix")

      posfix = self.model.infix2posfix(current_infix)
      self.view.inputsFrame.update_input(input_name="posfix", value=posfix)
      value = self.model.posfix2value(posfix)
      self.view.inputsFrame.update_input(input_name="value", value=value)
    else:
      current_infix = self.view.inputsFrame.get_input("infix")
      self.view.inputsFrame.update_input(input_name="infix", value=current_infix + ' ' + value + ' ')


  def run(self):
    self.view.mainloop()
