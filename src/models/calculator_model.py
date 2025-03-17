import math
from typing import Callable
from utils.queue import Queue
from utils.stack import Stack


class CalculatorModel:
  def __init__(self) -> None:
    self.functions: list[str] = ['log', 'sin', 'cos', 'tan', 'ln', 'alog', 'asin', 'acos', 'atan', 'aln']
    self.operators: list[str] = ['+', '-', 'x', '/', '^']


  def infix2posfix(self, expression: str) -> Queue[str]:
    priority: dict[str, int] = { fun: 4 for fun in self.functions } | { op: (i+2)//2 for i, op in enumerate(self.operators) }

    posfix: Queue[str] = Queue[str]()
    stack: Stack[str] = Stack[str]()

    for value in expression.split():
      if value in priority:
        
        while priority.get(stack.peek(), 0) >= priority.get(value, 0):
          posfix.enqueue(stack.pop())
        else:
          stack.push(value)
      elif value == '(':
        stack.push(value)
      elif value == ')':
        while (val := stack.pop()) and val != '(':
          posfix.enqueue(val)
      else:
        posfix.enqueue(value)

    while (val := stack.pop()):
      posfix.enqueue(val)

    return posfix

  
  def posfix2value(self, posfix: Queue[str]) -> int | float:
    stack: Stack[float] = Stack[float]()

    operators: dict[str, Callable[[float, float], float]] = {
      '+': lambda b, a: a+b,
      '-': lambda b, a: a-b,
      'x': lambda b, a: a*b,
      '/': lambda b, a: a/b,
      '^': lambda b, a: a**b
    }

    functions: dict[str, Callable[[float], float]] = {
      'sin': lambda x: math.sin(math.radians(x)),
      'cos': lambda x: math.cos(math.radians(x)),
      'tan': lambda x: math.tan(math.radians(x)),
      'log': lambda x: math.log10(x),
      'ln': lambda x: math.log(x),
      'asin': lambda x: math.degrees(math.asin(x)),
      'acos': lambda x: math.degrees(math.acos(x)),
      'atan': lambda x: math.degrees(math.atan(x)),
      'alog': lambda x: 10**x,
      'aln': lambda x: math.exp(x)
    }

    while (value := posfix.dequeue()):
      stack.push(
        functions[value](stack.pop()) if value in functions else
        operators[value](stack.pop(), stack.pop()) if value in operators else
        float(value)
      )
    
    return int(value) if (value := stack.pop()).is_integer() else value.__round__(2)
  