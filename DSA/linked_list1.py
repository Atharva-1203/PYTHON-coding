class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

a=Node(10) #Head node
b=Node(5)
c=Node(2)
a.next=b
b.next=c 


head=a
print(head.data)
print(head.next.data)

#Traversal
curr=head
while curr!=None:
    print(curr.data)
    curr=curr.next 