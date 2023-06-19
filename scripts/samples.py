# examples of useful things in the python language
#list comprehension
squares = []
for x in range(10):
    squares.append(x**2)

[x**2 for x in range(10)]

#advanced list comprehension
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

#list functions
listy = [1,2,4]
y = listy # shallow copy! y will pick up changes
y = listy[:] # deep copy - y will remain the same

for i,num in enumerate(listy):
    print(i,num)

def myFunction(x):
    return x < 3
filterList = filter(myFunction,listy)
for x in filterList:
    print(x)

print('SUM: ',sum(listy))


listy.append(5)
listy.sort() #in place
new_list = sorted(listy)
len(listy)

# tuples | cannot change add or remove items
atuple = ('apple','apple','zuchinni','cherry')
print(type(atuple))
w,x,y,z = atuple
print(f'value of w: {w}, value of x: {x}, value of y: {y}, value of z: {z}')

#sets | cannot change, can add or remove
aset = {1,2}
aset.add(1) # only appears once
aset.add('yo')
# access with for loop
for x in aset:
    print(x)

print(aset)

# dictionaries
adict = {
    1 : 'mohammed',
    2 : 'khaled', 
    3 : 'abdul'
}
# create dict items
adict.items()
adict.keys()
adict.values()
adict[1]='mike'
# adict[6] <-- Key Error!
print(adict.get(4)) # <-- returns null


#strings 
word = 'Hello!!'
w = word[3:]
i = w[3:].find('l') # returns -1
print('index: ',i)
# word.index('x') <-- Value Error!
word.isnumeric()
word.isalpha()
word.strip() # removes white spaces

phrase='here is a phrase'
phrase.split(' ')# splits into a sentence

#functions
def myfunc(var=1):
    return var * 2
#lambda functions
x = lambda a: a+10
print(x(5))

#examples
pairs = [(1,'c'),(2,'b'),(3,'a')]
pairs.sort(key=lambda x: -x[0]) # sort by reverse order of first item
pairs.sort(key=lambda x: x[1], reverse=True) # sort by reverse order of second item


#Ques
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
letter = q.popleft()
q.appendleft('a')


# Classes and Objects 
class Node:
    def __init__(self,val=0,next=None): # must include self, __init__ is the constructor
        self.val=val
        self.next=next

node1 = Node(1)
node2 = Node(2)
node1.next = node2

# HEAPS
# Heaps looks at first entry ex: (3,'A') - heapsorts on 3
# min heap only! for max heap multiply by -1
import heapq
sample = [2,6,4,1]
heapq.heapify(sample)
heapq.heappush(x,3)
heapq.heapppop(x)
heapq.heapreplace(x,2)
