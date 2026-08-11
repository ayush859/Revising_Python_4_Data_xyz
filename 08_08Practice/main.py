print("How are you")

""" Functions """


def hello():
    print("This is  a hello function so I am doing hello")

hello()



# Types of Argument

# Positional Argument
def sum(a,b):
    print(f"The  sum of your no is {a+b}")

sum(10,20)

# here we are using keyword argument , as we are selecting a key first then passing argument
def hello(name,age):
    print(f'yur name is {name} and your age is {age}')

hello(age = 23,name="Asamti")

# here we are using default argument
def sum(a, b =12):
    print(f'The sum is {a+b}')
sum(12)
sum(12,15)

def palindrome_chk(str):
     rev =''
     for i in range(len(str)-1,-1,-1):
         rev+=str[i]
     if str == rev:
         print(f"{str} is a palindrome")
     else:
         print(f"{str} is not a palidrome")

palindrome_chk('NAMAN')
palindrome_chk('CURSOR')

# Return use case

def hello():
    print("Hello How are you")
hello()

'''If a function uses return, use print() to display the returned value. If the function already uses print(), just call the function.'''
def hello():
    return "Hello How are you"

print(hello())



""" Data Structures """

# List Powers
'List are mutable , duplicates are allowed , data stored in sequential manner can be accessed via index , heterogenous data can be stored at one place'

list = [1 , 2.3 ,'a',True, print()]
print(list[-1])
#it will run but return NONE

list[0]=421
'''strings are not mutable ,but list are '''
print(list)

'''List Traversing and Methods'''

#1 way using index
a = [11 ,12 ,13 ,14, 15 ,16,23.4]
for i in range(len(a)):
    print(a[i])

#2 way directly on values
for i in a:
    print(i)

'''Method is also kind of function which is defined in a class'''

l = [1,3,2,4,5]

l.append(6) # add values to the end
l.insert(1,2) # insert 2 at 1st index
l.extend([7,8,9]) #add multiple elements at the end
l.remove(2) # removes the first occurence of 2
popped_item = l.pop(3) # removes and stores element at index 3(raise error if element not found )
find_ind = l.index(6)  # finds the index of the value 6
cnt_4 = l.count(4) # counts the occurence of 4
l.sort() # sort the list in ascending order
l.reverse() # reverses the original list order
l_new = l.copy() # used to store copy of original list
l_new.clear() # used to remove all the elements from the list


""" TUPLES """

tup = (10,20,30,40)
print(type(tup))

list = [10,20,30,40]
print(type(list))

''' Tuples are Immutable , duplicates are allowed ,   data stored in sequential manner can be accessed via index , heterogenous data can be stored at one place'''
'''tuples are like strings you can’t change anything once it’s made we can’t change them '''
tup = (1 , 7,2,3 , 4, 3, 2.3 ,'a',True, print())

''' there are only 2 methods of tuple one for finding the index and other of counting the occurrences of an element. '''
index = tup.index(3)
print(index)

count = tup.count(3)
print(count)

''' we can also use Tuple Unpacking '''
a,b,c,d = (1,2,3,4)
print(a,b,c,d)


a = (1)
print(type(a))

''' Values without a comma are unpacked normally. Adding a comma makes the value a tuple. '''

b = (1,)
print(type(b))

""" SET """

s={1,2,3,4,5}
''' set are Mutable, duplicates are not allowed , data are not stored in sequential manner and dont have index values , heterogenous data can be stored at one place  '''

'''Each value in a set is hashed using a hash function (hash() in Python)'''
''' Only immutable (hashable) objects can be stored in a set (e.g., numbers, strings, tuples). '''
'''Mutable objects like lists and dictionaries are not allowed '''

''' if we do hashing of values , it will be different each time '''

b = hash("hello")
print(b)

c = hash((1,2,344))
print(c)

'''A set cannot be traversed using the index values cause it is unordered and has no index'''

''' Integer hash values are stored in a way that often represents the integer itself. '''
s = {1,2,9,3,"hello",4,5,8,3}
for i in s:
    print(i)
'''  Set output order is not guaranteed and may differ. '''

# Set methods
s = {1,2,9,3,5}

s.add(0) # adds value at the end of the set
s.remove(2) # Removes 2 (raise error if element not found )
s.discard(5) # Removes 5 (same like remove )
popped_ele = s.pop() # Removes a random element
s.clear()  # Removes all the elements from the set


''' other operations
of sets that can be performed
between 2 sets. '''
a = {1,2,3,4,5}
b = {4,5,6,7,8}

s = a.union(b)
st = a|b
''' we can use union function or pipeline operator (|) '''
print(s)
print(st)


s = a.intersection(b)
st = a& b
print(s)
print(st)

s = a.difference(b)
st = a-b
print(s)
print(st)

''' symmetric difference is removing the common ones from both and joining them'''

s= a.symmetric_difference(b)
st = a^b
print(s)
print(st)

''' compound operations ,it means that doing operation inplace without using other ones '''
a = {1,2,3,4,5}
b = {4,5,6,7,8}

b -= a
print(b)

