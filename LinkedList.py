class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def AppendNode(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            curr = self.head
            while curr.next!=None:
                curr = curr.next
            curr.next = newNode

    def PrintList(self):
        curr = self.head
        print("The linked list is: ")
        while curr!=None:
            print("|" + str(curr.data) + "|->", end = '')
            curr = curr.next
        print("NULL")

    def InsertNodeAtTheBeginning(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    def InsertNodeAtPosition(self, data, position):
        if position == 1:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            counter = 1
            curr = self.head
            newNode = Node(data)
            while counter!=position-1:
                curr = curr.next
                counter+=1
            newNode.next = curr.next
            curr.next = newNode

    def DeleteNode(self, position):
        prev = self.head
        curr = self.head.next
        counter = 1
        while counter!= position-1:
            prev = prev.next
            curr = curr.next
            counter+=1
        prev.next = curr.next

    def SearchByValue(self, data):
        curr = self.head
        counter = 1
        while curr.data!=data:
            curr = curr.next
            counter+=1
        return counter

    def ValueAtPosition(self, position):
        counter = 1
        curr = self.head
        while counter!=position:
            curr = curr.next
            counter+=1
        return curr.data

    def MakeCircular(self):  # Infinite Loop
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = self.head
