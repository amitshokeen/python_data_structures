class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def print(self):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print("<->".join(values))

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(9)
my_doubly_linked_list.append(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.print()




