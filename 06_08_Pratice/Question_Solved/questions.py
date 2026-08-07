input_take = input("Enter a number: ")

age = int(input("Enter your age: "))
print(age)


""" Conditional Questions """

#1 Accept two numbers and print the greater one.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a>b:
    print(a)
else:
    print(b)


#2 Accept gender and print the appropriate greeting.
# Example: Good Morning Sir / Good Morning Ma'am
gender = input("Enter your gender (Male/Female): ")

if gender == 'Male' or gender=="M":
    print("Good Morning Sir")
elif gender == 'Female' or gender ==  'F':
    print("Good Morning Maam")
else:
    print("Invalid gender")


#3 Accept a number and check whether it is even or odd.
num = int(input("Enter a number: "))

if num %2 ==0 :
    print("The number is even")
else:
    print("The number is odd")


#4 Accept name and age. Check whether the user is eligible to vote.
# Example: Hello Shery, you are a valid voter.
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age>=18:
    print(f'Hello {name}, you are a valid voter.')
else:
    print(f'Hello {name}, you are not a valid voter.')


#5 Accept a year and check whether it is a leap year.
year = int(input("Enter a year: "))

if(year%4 ==0) and (year %100 != 0):
    print("It is a leap year")
elif year%100 ==0 and year%400 ==0:
    print("It is a leap year")
else:
    print("It is a normal year")


temp = int(input("Enter the temperature: "))

if temp<0:
    print("Freezing Cold")
elif 0 <= temp < 10:
    print("Very Cold")
elif 10 <= temp < 20:
    print("Cold")
elif 20 <= temp < 30:
    print("Pleasant")
elif 30 <= temp < 40:
    print("Hot")
else:
    print("Very Hot")