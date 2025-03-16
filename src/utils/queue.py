from .node import Node
from typing import Generic, TypeVar

T = TypeVar('T')


class Queue(Generic[T]):
  def __init__(self) -> None:
    self.first: Node[T] | None = None
    self.last: Node[T] | None = None


  def enqueue(self, data: T) -> None:
    new_node: Node[T] = Node[T](data)

    if not self.first:
      self.first = new_node
      self.last = new_node
      return
    
    self.last.next = new_node
    self.last = new_node


  def dequeue(self) -> T | None:
    if not self.first:
      return None

    data: T | None = self.first.data
    self.first = self.first.next

    return data
