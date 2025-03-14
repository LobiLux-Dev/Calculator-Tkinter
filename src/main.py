from view.calculator_view import CalculatorView
from models.calculator_model import CalculatorModel

if __name__ == '__main__':
  # view = CalculatorView()
  # view.mainloop()
  model = CalculatorModel()

  # print(model.infix2posfix('2 * ( 2 ^ 3 * 2 - 6 / ( 4 - 2 ) - 10 ) - 2'))

  # print(model.posfix2value(model.infix2posfix('5 * ( 6 + 2 ) - 12 / 4')))
  # print(model.posfix2value(model.infix2posfix('4 - 3 ^ 2 / 3 + 7 * ( 1 - 2 )')))
  # print(model.posfix2value(model.infix2posfix('2 * ( 2 ^ 3 * 2 - 6 / ( 4 - 2 ) - 10 ) - 2')))
  # print(model.posfix2value(model.infix2posfix('2 ^ 4 / ( 4 * 1 ) + log ( 110 - 10 ) ^ 2')))
  # print(model.posfix2value(model.infix2posfix('2 + asin ( 1.7071 - 1 ) + 3')))
  # print(model.posfix2value(model.infix2posfix('sin ( 45 ) ^ 2 + cos ( 45 ) ^ 2')))
  # print(model.posfix2value(model.infix2posfix('sin ( 45 )')))
  # print(model.posfix2value(model.infix2posfix('asin ( 0.71 )')))
  # print(model.posfix2value(model.infix2posfix('( -8 + ( 8 ^ 2 - 4 * 1 * 15 ) ^ 0.5 ) / ( 2 * 1 )')))
