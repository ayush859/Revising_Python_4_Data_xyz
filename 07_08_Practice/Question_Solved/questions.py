from numpy.lib.scimath import sqrt
import random

""" For Loop Questions """

#1 Accept an integer and print "Hello World" n times.
n = int(input("Enter a number: "))

for i in range(n):
    print("Hello World")

print("---------------------------------")

#2 Print natural numbers up to n.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)

print("---------------------------------")

#3 Print numbers from n to 1.
n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    print(i)

print("---------------------------------")

#4 Accept a number and print its multiplication table.
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("---------------------------------")

#5 Find the sum of first n natural numbers.
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(f"Sum of first {n} natural numbers is {sum}")

print("---------------------------------")

#6 Find the factorial of a number.
n = int(input("Enter a number: "))

fact = 1

for i in range(2, n + 1):
    fact *= i

print(f"Factorial of {n} is {fact}")

print("---------------------------------")

#7 Print the sum of all even and odd numbers separately up to n.
n = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Even sum till {n} is {even_sum}")
print(f"Odd sum till {n} is {odd_sum}")

print("---------------------------------")

#8 Print all the factors of a number.
n = int(input("Enter a number: "))

print(f"Factors of {n} are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

print("---------------------------------")

#9 Check whether a number is a perfect number.
n = int(input("Enter a number: "))

fact_sum = 0

for i in range(1, n):
    if n % i == 0:
        fact_sum += i

if fact_sum == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

print("---------------------------------")

#10 Check whether a number is prime.
n = int(input("Enter a number: "))

is_prime = True

if n < 2:
    is_prime = False
else:
    sqrt_val = int(sqrt(n))
    for i in range(2, sqrt_val + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

print("---------------------------------")

#11 Reverse a string without using built-in functions.
text = input("Enter a string: ")

rev_str = ""

for i in range(len(text) - 1, -1, -1):
    rev_str += text[i]

print(f"Reverse of {text} is {rev_str}")

print("---------------------------------")

#12 Check whether a string is a palindrome.
text = input("Enter a string: ")

is_palindrome = True

for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")

print("---------------------------------")

#13 Count letters, digits, and special characters in a string.
text = "P@#yn26at^&i5ve"

cnt_char = 0
cnt_digit = 0
cnt_symbol = 0

for ch in text:
    if ch.isalpha():
        cnt_char += 1
    elif ch.isdigit():
        cnt_digit += 1
    else:
        cnt_symbol += 1

print(f"String: {text}")
print(f"Letters: {cnt_char}")
print(f"Digits: {cnt_digit}")
print(f"Special Symbols: {cnt_symbol}")

""" While Loop Questions """

#1 Separate each digit of a number and print it on a new line.
num = int(input("Enter a number: "))

while num > 0:
    print(num % 10)
    num //= 10      # // removes the last digit.

print("---------------------------------")

#2 Accept a number and print its reverse.
num = int(input("Enter a number: "))

original = num
rev_num = 0

while num > 0:
    rev_num = rev_num * 10 + num % 10
    num //= 10

print(f"Reverse of {original} is {rev_num}")

print("---------------------------------")

#3 Check whether a number is a palindrome.
if original == rev_num:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")

print("---------------------------------")

#4 Create a random number guessing game.
num = random.randint(1, 10)
tries = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1

    if guess < num:
        print("Guess a little higher.")
    elif guess > num:
        print("Guess a little lower.")
    else:
        print(f"You guessed the correct number in {tries} tries.")
        break