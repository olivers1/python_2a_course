from typing import Any, Iterable

class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.prev: Node = None
        self.next: Node = None


class SimpleQueue:
    def __init__(self, iterable: Iterable[Any]) -> None:
        for value in iterable:
            self._tail = Node(value)
            try:
                self._tail.next = node
            except UnboundLocalError:
                node = self._tail
                self._head = node
            else:
                self._tail.next = node
                node.prev = self._tail
                node = self._tail

    def __bool__(self) -> bool:
        return self._head is not None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        try:
            # this part succeeds if instance of SimpleQue contains at least one Node
            new_node.next = self._tail
            self._tail.prev = new_node
        except AttributeError:
            # if instance of SimpleQue is empty, new_node becomes the first and only Node. Thus it is becoming both head and tail
            self._head = new_node
        self._tail = new_node

    def popleft(self) -> Any:
        # deletes head node (node most to the left in list) and return its value
        value = self._head.value
        self._head = self._head.prev
        # set next and prev parameters for the new head node after the previous head node has been popped
        try:
            # if list is empty this line of code will fail, except case will run and throw an error
            self._head.next = None
        except AttributeError:
            pass
        return value


"""
simple_list = SimpleQueue([5, 7, 3])

print(simple_list.popleft())
print(simple_list.popleft())
print(simple_list.popleft())
print(simple_list.popleft())
"""