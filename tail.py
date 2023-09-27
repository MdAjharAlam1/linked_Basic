class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_tail(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data,end=" ")
            current_node = current_node.next

llist = Linkedlist()
arr = [1,2,3,4,44]
for i in range(len(arr)):
    llist.insert_tail(arr[i])

llist.printLL()