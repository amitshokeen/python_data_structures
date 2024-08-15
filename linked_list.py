class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def print(self):
        if self.head == None:
            print("empty list")
        else:
            temp = self.head
            values = []
            while temp is not None:
                values.append(str(temp.value))
                temp = temp.next
            print("->".join(values))

    def remove_duplicates(self):
        # since a python set cannot have duplicates, we make use of this in-built data structure
        values = set()
        previous = None
        current = self.head
        if self.head is None:
            return None
        while current is not None:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

ll = LinkedList(3)
ll.append(5)
ll.append(3)
ll.append(7)
ll.append(8)
ll.append(5)
ll.append(9)
ll.print()
ll.remove_duplicates()
ll.print()