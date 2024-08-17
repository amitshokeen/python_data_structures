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

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp  = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1      
            return temp  
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
            self.length -= 1
            return temp
        
    def get(self, index):
        if self.length == 0:
            return None
        elif index < 0 or index >= self.length:
            print("Index out of bounds")
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        if self.length == 0:
            return None
        elif index < 0 or index >= self.length:
            print("Index out of bounds")
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        temp.value = value
        return temp

class Test:
    def test_pop():
        my_doubly_linked_list = DoublyLinkedList(7)
        my_doubly_linked_list.append(4)
        my_doubly_linked_list.append(3)
        my_doubly_linked_list.append(9)
        my_doubly_linked_list.append(0)
        my_doubly_linked_list.append(1)
        my_doubly_linked_list.print()
        popped = my_doubly_linked_list.pop()
        print(popped.value)
        my_doubly_linked_list.print()

        dll = DoublyLinkedList(6)
        dll.print()
        print(dll.pop().value)
        dll.print()    

    def test_prepend():
        my_doubly_linked_list = DoublyLinkedList(7)
        my_doubly_linked_list.append(4)
        my_doubly_linked_list.append(3)
        my_doubly_linked_list.append(9)
        my_doubly_linked_list.append(0)
        my_doubly_linked_list.append(1)
        my_doubly_linked_list.print()
        my_doubly_linked_list.prepend(2)
        my_doubly_linked_list.print()

    def test_pop_first():
        dll = DoublyLinkedList(7)
        dll.append(4)
        dll.print()
        print(dll.pop_first().value)
        dll.print()
        print(dll.pop_first().value)
        dll.print()

    def test_get():
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        dll.append(5)
        try:
            print(dll.get(0).value)
            print(dll.get(1).value)
            print(dll.get(2).value)
            print(dll.get(3).value)
            print(dll.get(4).value)
            print(dll.get(5).value)
        except Exception as e:
            print("Exception raised:", e)

    def test_set_value():
        dll = DoublyLinkedList(3)
        dll.append(4)
        dll.append(1)
        try:
            print(dll.set_value(2,9).value)
            print(dll.print())
            print(dll.set_value(7,0).value)
            print(dll.print())
        except Exception as e:
            print("Exception raised:", e)




# Test.test_pop()
# Test.test_prepend()
# Test.test_pop_first()
# Test.test_get()
Test.test_set_value()


