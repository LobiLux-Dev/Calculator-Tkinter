from view.calculator_view import CalculatorView
from models.calculator_model import CalculatorModel

if __name__ == '__main__':
  view = CalculatorView()
  view.mainloop()

'''
  model = CalculatorModel()

  expressions = [
    '5 * ( 6 + 2 ) - 12 / 4',
    '4 - 3 ^ 2 / 3 + 7 * ( 1 - 2 )',
    '2 * ( 2 ^ 3 * 2 - 6 / ( 4 - 2 ) - 10 ) - 2',
    '2 ^ 4 / ( 4 * 1 ) + log ( 110 - 10 ) ^ 2',
    '2 + asin ( 1.7071 - 1 ) + 3',
    'sin ( 45 ) ^ 2 + cos ( 45 ) ^ 2',
    'sin ( 45 )',
    'asin ( 0.71 )',
    '( -8 + ( 8 ^ 2 - 4 * 1 * 15 ) ^ 0.5 ) / ( 2 * 1 )'
  ]

  for expression in expressions:
    posfix = model.infix2posfix(expression)
    print(f"Expression: {expression}")
    print(f"Posfix: {posfix.first}")

    value = model.posfix2value(posfix)
    print(f"Value: {value}")
    print()'''
