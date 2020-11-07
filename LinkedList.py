class ListNode:
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next
    
    #Function inserts Node after node it was called on
    def insertNode(self, node):
        self.next, node.next = node, self.next
    
    #Print the contents of a linked list
    def printList(self):
        node = self
        while(node):
            print(node.val)
            node = node.next
  
class ListAlgos():

    #Takes an array and converts it into a linked list
    def arraytolist(self, array):
        node = ListNode(array[0])
        head = node
        for i in range(1,len(array)):
            node.next = ListNode(array[i])
            node = node.next
        
        return head

    #Reverses linked list
    def reverseList(self, head):
        prevNode = None
        currNode = head
        while(currNode):
            temp1 = currNode.next
            temp2 = currNode
            currNode.next = prevNode
            currNode = temp1
            prevNode = temp2
        
        return prevNode


#Test cases for Linked list data structures
s = ListAlgos()
test=[1,2,5,6,7]
list1 = s.arraytolist(test)
list1.printList()
reverse = s.reverseList(list1)
print('reverse!')
reverse.printList()