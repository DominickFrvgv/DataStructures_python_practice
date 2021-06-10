# Practicing by looking at the steps

# append, length, display, addbeginning 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next 

        last.next = new_node

    def length(self):
        if self.head == None:
            return 0

        last = self.head
        counter = 0
        while last:
            counter += 1
            last = last.next

        return counter

    def toList(self):
        elem = []
        curr_node = self.head
        while curr_node:
            elem.append(curr_node.data)
            curr_node = curr_node.next
        return elem

    def display(self):
        if self.head == None:
            return 'empty list'
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        return '--'

    def addBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node

# testing..

a = Linked_List()
print(a.display())
a.append(3)
a.append(37)
a.addBeginning(2)
a.append(6)
print(a.length())
a.append(7)
a.append(8)
print(a.length())
print(a.toList())
print(a.display())