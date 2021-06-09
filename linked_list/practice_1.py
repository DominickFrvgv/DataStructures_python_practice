# Practicing by looking at the steps

# append & length
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


# testing..

a = Linked_List()
a.append(3)
a.append(37)
a.append(6)
print(a.length())
a.append(7)
a.append(8)
print(a.length())

