# ! find the length of linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
    def find_length(self):
        temp = 0
        curr = self.head
        while(curr!=None):
            temp+=1
            curr = curr.next
        print("lenght of linked_list :- ",temp)
    def inser_tail(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
            return self.head
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = new_node 
        return self.head 



llist = LinkedList()

llist.insert_node('a')
llist.insert_node('b')
llist.insert_node('c')
llist.insert_node('d')
llist.insert_node('g')
# print(llist.insert_node())
print()
print()
arr = [1,2,3,4,6]
for i in range(len(arr)):
    print(llist.inser_tail(arr[i]))
print(llist.inser_tail(1))
print(llist.inser_tail(2))
print(llist.inser_tail(3))
print(llist.inser_tail(4))
print(llist.inser_tail(5))
# print the linked list
print("Node Data")
llist.printLL()
llist.find_length()
 
