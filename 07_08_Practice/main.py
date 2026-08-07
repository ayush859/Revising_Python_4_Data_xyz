"""" Range Function """

''' The range() function takes start, stop, and step values. Only the stop value is mandatory. If start is omitted, it defaults to 0. If step is omitted, it defaults to 1. '''

a = range(1,20,1)

# for i in a:
# print(i)

# for i in range(20,1,-1):
# print(i)

n = int(input("Which table do you want? "))

for i in range(n,(n*10)+1,n):
print(i)

''' There are two ways to iterate through a string. '''

''' 1. Using range() -> Gives the index (position) of each character. '''
for i in range(len(a)):
print(i, a[i])

''' 2. Without using range() -> Gives the characters directly. '''
for ch in a:
print(ch)

''' Break Statement '''

for i in range(1,21):
if i == 12:
break
print(i)