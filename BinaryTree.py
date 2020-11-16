'''
BINARY TREE
This file implments many binary tree algorithms
-CLASSES-
    TreeNode: Defines how to create and manipulate the tree
    TreeAlgos: Example Algorithms that can be used on a binary tree
'''
class TreeNode:
    #Constructor: tree node that can also point to its left and right components
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    #Insert node into binary tree
    def insert(self, node):
        baseNode = self
        if baseNode.val >= node.val:
            if not baseNode.left: baseNode.left = node
            else: baseNode.left.insert(node)
        elif baseNode.val < node.val:
            if not baseNode.right: baseNode.right = node
            else: baseNode.right.insert(node)

class TreeAlgos:

    '''
    Tree Algorithms: Different Tree Algorithm implmentation
        Treeify: Turns list into a binary
        depthTraversal: implements depth first search
        breadthTraversal: implements breadth first search search
        maxDepth: Find the tree depth
        invertTree: reverse the order of the Tree
    '''

    def Treeify(self, array):
        if not array: return
        length = len(array)
        def helper(index):
            node = TreeNode(array[index])
            Li, Ri = index*2 + 1, index*2 + 2
            if Li < length and array[Li]: node.left = helper(Li)
            if Ri < length and array[Ri]: node.right = helper(Ri)

            return node
        
        return helper(0)

    def depthTraversal(self, node):
        if node.left:
            self.depthTraversal(node.left)
        
        print(node.val)

        if node.right:
            self.depthTraversal(node.right)
    
    def breadthTraversal(self, node):
        q = []
        q.append(node)
        while q:
            currNode = q.pop(0)
            print(currNode.val)
            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
    
    def maxDepth(self, node):
        if not node: return 0
        L = 1 + self.maxDepth(node.left)
        R = 1 + self.maxDepth(node.right)

        return max(L,R)

    def invertTree(self, node):
        q = [node]
        root = node

        while q:
            currNode = q.pop(0)
            currNode.left, currNode.right = currNode.right, currNode.left
            if currNode.left: q.append(currNode.left)
            if currNode.right: q.append(currNode.right)
    
    # Converts a tree into a linked list in place
    def Listify(self, root):
        if not root: return
        spare = []
        
        def helper(node):
            if node.left and node.right:
                spare.insert(0,node.right)
                node.right = node.left
                node.left = None
                
            elif node.left:
                node.right, node.left = node.left, node.right
            
            elif not node.right and spare:
                node.right = spare.pop(0)
    
            if node.right: helper(node.right)
            return
        
        helper(root)
        
        return root


a = TreeAlgos()
#Test Binary Tree
test = [3,9,20,None,None,15,7]
root = a.Treeify(test)

#Test Algorithms
print(a.maxDepth(root))
print("Depth Traversal")
a.depthTraversal(root)
print("Breadth Traversal")
a.breadthTraversal(root)
a.invertTree(root)