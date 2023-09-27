# insert node from the tail of single linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None

    def insert_tail(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return self.head
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node
        return self.head
    
    def printLL(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.data,end=" ")
            curr_node = curr_node.next
        
llist = linkedlist()
arr = [1,2,4,5,5]
for i in range(len(arr)):
    llist.insert_tail(arr[i])


llist.printLL()