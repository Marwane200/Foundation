
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
word = '   Hello!!   '
word.find('z') # returns -1
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



# Classes and Objects 
class Node:
    def __init__(self,val=0,next=None): # must include self, __init__ is the constructor
        self.val=val
        self.next=next

node1 = Node(1)
node2 = Node(2)
node1.next = node2


num = None
if not num: print('NOTTTYY')