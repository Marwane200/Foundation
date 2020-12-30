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
    
    def insertWord(self, word: str):
        node = self.root
        for c in word:
            node.children[c] = node.children.get(c,TrieNode(c))
            node = node.children[c]

        node.isWord=True
    
    def printTrie(self):
        words = []
        node = self.root
        def dfs(word: str, node: TrieNode):
            w = word + node.char
            if node.isWord: words.append(w)
            for n in node.children.values():
                dfs(w,n)
        dfs('',node)
        [print(word, end=' ') for word in words]


#Test Cases

test = ['adder','ackman','always','doubter','macaroni','tin','marshin','window','cloud']  
trie = Trie()
[trie.insertWord(word) for word in test]
trie.printTrie()