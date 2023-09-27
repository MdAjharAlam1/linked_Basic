# add node to the begninig of linkedlist
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_front(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self.head
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head
 
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

llist = Linkedlist()
arr = [1,2,3,4,4,5,5]
for i in range(len(arr)):
    llist.insert_front(arr[i])
llist.printLL()