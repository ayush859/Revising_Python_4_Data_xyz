a = 56/3
print(type(a))

# Data Types

""" Strings """

''' You can use either double quotes ("") or single quotes (''). Both work the same. '''

## Finding Unicode value of a character

char = 'A'
print(ord(char))

''' ord() works only with a single character. '''

a = "SHER"

print(a[-1], a[3])


""" String Slicing """

'''
String slicing uses start, stop, and step.

Syntax:
string[start : stop : step]

Note:
The stop index is excluded.
For example, stop = 4 means slicing ends at index 3.
'''

a = "SHER CODE"

print(a[0:4:1])
print(a[::])


""" Type Conversion """

''' There are two types of type conversion:
1. Implicit Conversion
2. Explicit Conversion
'''

'''
Python has Truthy and Falsy values.

Only these 7 values are considered False:
0
0.0
False
""
[]
{}
()

Everything else is converted to True.
'''

a = 12
print(type(a))

a = str(a)
print(type(a))


# Implicit Conversion

a = 12
print(type(a))

print(type(a/3))


# Explicit Conversion

'''
In explicit conversion, we use built-in functions
to convert one data type into another.

int()      -> Integer
float()    -> Float
complex()  -> Complex
str()      -> String
list()     -> List
tuple()    -> Tuple
set()      -> Set
dict()     -> Dictionary
bool()     -> Boolean
'''


""" Input and Output """

# Two ways to print output

name = "qt_alr"
age = 18

print("The name is", name, "and age is", age)

# Formatted strings (f-strings) make output cleaner and allow expressions.
print(f"The name is {name} and age is {age}")


'''
input() is used to take input from the user.

If the value is not stored, it is discarded.

By default, input() always returns a string,
so sometimes we need explicit type conversion.
'''

age = input("Enter your age: ")
print(type(age))

age = int(input("Enter your age: "))
print(type(age))


""" Arithmetic Operators """

'''
There are 7 arithmetic operators.

+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor Division
%   Modulus
**  Exponentiation
'''

print(20/5)
print(20//5)


""" Compound Assignment Operators """

'''
+=   Add and assign
-=   Subtract and assign
*=   Multiply and assign
/=   Divide and assign
//=  Floor divide and assign
%=   Modulus and assign
**=  Exponentiate and assign
'''

a = 20
a += 20
a **= 2


""" Comparison Operators """

'''
Comparison operators always return a Boolean value
(True or False).

They work with numbers as well as strings.

When comparing strings, Python compares their Unicode values.

Python can compare int, float, and complex where supported.
'''

print(ord("A"))
print(ord("B"))
print("A" > "B")


""" Logical Operators """

'''
There are 3 logical operators.

and  -> Returns True if both conditions are True.
or   -> Returns True if at least one condition is True.
not  -> Reverses the Boolean value.
'''

print(123 > 100 and 22 == 22)
print(not 122 == 122)


""" Conditional Statements """

'''
if
    Executes a block only if the condition is True.

if-else
    Executes one block if the condition is True,
    otherwise executes another block.

if-elif-else
    Checks multiple conditions in order and
    executes the first matching block.
'''