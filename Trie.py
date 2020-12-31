'''
TRIE
this implements a TRIE datastructure which is useful for word search and prefixes
-CLASSES-
    TrieNode: instantiates a single tree node
    Trie: instantiates the trie class with algorithms to manupilate the words
'''

class TrieNode:
    def __init__(self, char=''):
        self.char=char
        self.children={}
        self.isWord=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    
    #Inserts words into Trie Structure
    def insertWord(self, word: str):
        node = self.root
        for c in word:
            node.children[c] = node.children.get(c,TrieNode(c))
            node = node.children[c]

        node.isWord=True
    
    #Prints out all word in the Trie
    def printTrie(self, n=None, pre=''):
        words = []
        if n: node = n
        else: node = self.root
        def dfs(word: str, node: TrieNode):
            w = word + node.char
            if node.isWord: words.append(w)
            for n in node.children.values():
                dfs(w,n)
        dfs(pre,node)
        [print(word, end=' ') for word in words]
        print('')
    
    #Prints out all words with a prefix
    def prefix(self, prefix: str):
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if not node:
                print('No word with prefix: ' + prefix)
                return None
        
        self.printTrie(node,prefix[:-1])

#Test Cases

test = ['adder','ackman','always','doubter','macaroni','tin','marshin','window','cloud']  
trie = Trie()
[trie.insertWord(word) for word in test]
trie.printTrie()
trie.prefix('a')