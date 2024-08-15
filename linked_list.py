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

    def partition_list(self, x):
        if self.head is None:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
        while current.next is not None:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next
        self.head = dummy1.next
        return True

ll = LinkedList(3)
ll.append(5)
ll.append(3)
ll.append(7)
ll.append(8)
ll.append(5)
ll.append(9)
ll.append(1)
ll.print() # 3->5->3->7->8->5->9->1
#ll.remove_duplicates()
ll.print() # 3->5->7->8->9->1
ll.partition_list(7)
ll.print()