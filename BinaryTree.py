class TreeNode:
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


root = TreeNode(7)
root.insert(TreeNode(3))
root.insert(TreeNode(9))
root.insert(TreeNode(4))
root.insert(TreeNode(12))
root.insert(TreeNode(10))


a = TreeAlgos()
a.depthTraversal(root)