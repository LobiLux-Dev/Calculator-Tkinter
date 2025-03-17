import math
from typing import Callable
from utils.queue import Queue
from utils.stack import Stack


class CalculatorModel:
  def __init__(self) -> None:
    self.functions: dict[str, Callable[[float], float]] = {
      'alog': lambda x: 10**x,
      'ln': lambda x: math.log(x),
      'aln': lambda x: math.exp(x),
      'log': lambda x: math.log10(x),
      'sin': lambda x: math.sin(math.radians(x)),
      'cos': lambda x: math.cos(math.radians(x)),
      'tan': lambda x: math.tan(math.radians(x)),
      'asin': lambda x: math.degrees(math.asin(x)),
      'acos': lambda x: math.degrees(math.acos(x)),
      'atan': lambda x: math.degrees(math.atan(x))
    }
    
    self.operators: dict[str, Callable[[float, float], float]] = {
      '+': lambda b, a: a+b,
      '-': lambda b, a: a-b,
      'x': lambda b, a: a*b,
      '/': lambda b, a: a/b,
      '^': lambda b, a: a**b
    }


  def infix2posfix(self, infix: str) -> str:
    priority: dict[str, int] = { **{ fun: 4 for fun in self.functions }, **{ op: (i+2)//2 for i, op in enumerate(self.operators) } }

    queue: Queue[str] = Queue[str]()
    stack: Stack[str] = Stack[str]()

    for value in infix.split():
      if value in priority:
        while priority.get(stack.peek(), 0) >= priority.get(value, 0):
          queue.enqueue(stack.pop())
        stack.push(value)
      elif value == '(':
        stack.push(value)
      elif value == ')':
        while (val := stack.pop()) != '(':
          queue.enqueue(val)
      else:
        queue.enqueue(value)

    while val := stack.pop():
      queue.enqueue(val)

    posfix: list[str] = []

    while value := queue.dequeue():
      posfix.append(value)

    return " ".join(posfix)

  
  def posfix2value(self, posfix: str) -> int | float:
    stack: Stack[float] = Stack[float]()

    for value in posfix.split():
      stack.push(
        self.functions[value](stack.pop()) if value in self.functions else
        self.operators[value](stack.pop(), stack.pop()) if value in self.operators else
        float(value)
      )
    
    return int(value) if (value := stack.pop()).is_integer() else value.__round__(2)
