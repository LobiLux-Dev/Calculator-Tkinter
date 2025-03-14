from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
  def __init__(self, data: T, head: Optional["Node[T]"]) -> None:
    self.data = data
    self.next = head


  def __str__(self) -> str:
    return f"{self.data}" + (', ' + str(self.next) if self.next else '')
