from .node import Node
from typing import Generic, TypeVar

T = TypeVar('T')


class Stack(Generic[T]):
  def __init__(self) -> None:
    self.top: Node[T] | None = None

  
  def push(self, data: T) -> None:
    self.top = Node[T](data, self.top)


  def pop(self) -> T | None:
    if not self.top:
      return None

    current = self.top
    self.top = current.next

    return current.data
  

  def peek(self) -> T | None:
    if not self.top:
      return None
    
    return self.top.data

  
  def __str__(self) -> str:
    return f"[{self.top}]"
