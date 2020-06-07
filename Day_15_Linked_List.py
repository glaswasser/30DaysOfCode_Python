# Complete the insert function in your editor so that it creates a new Node
# (pass data as the Node constructor argument) and inserts it at the tail of the
# linked list referenced by the head parameter. Once the new node is added,
# return the reference to the head node.
# Note: If the head argument passed to the insert function is null,
# then the initial list is empty.

###
# okay so I still don't think I fully get everything about this, but I managed to
# do it with this general tutorial:
# https://www.youtube.com/watch?v=JlMyYuY1aXU
# and this also helps about the idea:
# https://www.youtube.com/watch?v=JlMyYuY1aXU

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        if head == None:
            head = Node(data)
        else:
            current = head
            while current.next != None:
                current = current.next
            # once we reach the next = none we get to a new Node:
            current.next = Node(data)
        return head


    #Complete this method


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
