'''
LINKED LIST

Linked List is another foundational data structure that is good for creating dynamic lists.
This file is broken up into 2 parts:
ListNode:
    -initialize list
    -insert node
    -remove node
    -print node

List Algorithms:
    -Array to Linked List
    -Reverse List
'''

class ListNode:
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next
    
    #Function inserts Node after node it was called on
    def insertNode(self, node):
        self.next, node.next = node, self.next
    
    #Remove node
    def delNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

    
    #Print the contents of a linked list
    def printList(self):
        node = self
        while(node):
            print(node.val)
            node = node.next
  
class ListAlgos():

    #Takes an array and converts it into a linked list
    def arraytolist(self, array):
        head = ListNode(array[0])
        node = head
        for val in array[1:]:
            node.next = ListNode(val)
            node = node.next
        
        return head

    #Reverses linked list
    def reverseList(self, head):
        prevNode = None
        currNode = head
        while(currNode):
            currNode.next, currNode, prevNode = prevNode, currNode.next, currNode
        
        return prevNode


#Test cases for Linked list data structures
algorithms = ListAlgos()
test=[1,2,5,6,7]

#Create a linked list from an array
list1 = algorithms.arraytolist(test)
list1.printList()

#reverse the linked list
reverse = algorithms.reverseList(list1)
reverse.printList()