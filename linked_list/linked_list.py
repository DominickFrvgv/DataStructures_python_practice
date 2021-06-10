

class Node:
    def __init__(self, data):
      self.data = data
      self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # check if list is empty
        if self.head == None:
            self.head = new_node
            return

        last_node = self.head
        # while is true until reaches the end of the list
        while last_node.next:
            last_node = last_node.next

        # point the last node to the new node
        last_node.next = new_node
        return

    def length(self):
        if self.head == None:
            return 0

        current_node = self.head
        cont = 0
        while current_node:
            cont += 1
            current_node = current_node.next

        return cont

    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next

        return node_data

    def display(self):
        contents = self.head

        if contents is None:
            print('List has no element')

        while contents:
            print(contents.data)
            contents = contents.next
        return '*-*'

    def reverseLinkedList(self):
        previous_node = None
        current_node = self.head

        while current_node != None:
            next = current_node.next 
            current_node.next = previous_node
            previous_node = current_node
            current_node = next
        self.head = previous_node

    def addBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node

    def removeNode(self, key):
        current_node = self.head
        
        # check if the head is the key
        if current_node is not None:
            if current_node.data == key:
                self.head = current_node.next
                current_node = None
                return

        while current_node is not None:
            if current_node.data == key:
                break
            prev_node = current_node
            current_node = current_node.next

        if current_node == None:
            return 'this key is not in the list'

        prev_node.next = current_node.next
        current_node = None


# tests
testList = Linked_List()

testList.append(3)
print(testList.length())
testList.append(5)
testList.append(10)
testList.append(25)
testList.append(7)
print(testList.to_list())
print(testList.display())
print(testList.length())
testList.reverseLinkedList()
testList.addBeginning(6)
print(testList.to_list())