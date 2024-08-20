import pytest
from doubly_linked_list import DoublyLinkedList

# test for popping a doubly linked list with just one node
def test_pop_one_node():
    dll1 = DoublyLinkedList(1)
    assert dll1.pop().value == 1
    assert dll1.head == None
    assert dll1.tail == None
    assert dll1.length == 0

# test for popping a doubly linked list with no value
def test_pop_no_node():
    dll1 = DoublyLinkedList(1)
    dll1.pop()
    assert dll1.pop() == None
    assert dll1.length == 0
    