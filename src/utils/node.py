from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
  def __init__(self, data: T, next: Optional["Node[T]"] = None) -> None:
    self.data = data
    self.next = next


  def __str__(self) -> str:
    return f"{self.data}" + (', ' + str(self.next) if self.next else '')
