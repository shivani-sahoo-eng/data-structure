
'''1.Even or Odd: Write a program that checks if a given number is even or odd using if-elif-else 
statements.'''
# num =int(input('Enter a num:-'))
# if num%2==0:
#     print('even')
# else:
#     print('odd')

# Score >= 90: Grade A
# 80 <= Score < 90: Grade B
# 70 <= Score < 80: Grade C
# 60 <= Score < 70: Grade D
# Score < 60: Grade F'''



'''2.Grading System: Write a program that takes a student('s score and outputs their grade using the following '
'conditions.
# Score >= 90: Grade A
# 80 <= Score < 90: Grade B
# 70 <= Score < 80: Grade C
# 60 <= Score < 70: Grade D
# Score < 60: Grade F'''

# num=int(input('enter your grade:-'))
# if num>= 90:
#     print(f'{num}Grade A')
# elif 80 <=num and num < 90:
#     print(f'{num}Grade B')
# elif 70 <= num and num< 80:
#     print(f'{num}Grade C')
# elif 60 <=num and num< 70:
#     print(f'{num}Grade D')
# else: print(f'{num}Grade F')

'''3.Number Sign Check: Write a Python program that checks whether a given number 
is positive, negative, or zero.'''


# num=int(input('enter your number:-'))
# if num>0:
#     print(f'{num}positive')
# elif num < 0:
#     print(f'{num}negative')
# else: print(f'{num}zero')

# or

# num=input('enter your number:-')
# if num.startswith('+'):
#     print(f'{num}positive')
# elif num.startswith('-'):
#     print(f'{num}negative')
# else: print(f'{num}zero')


'''4.Age-Based Movie Rating: Write a program that asks for a user's age and suggests a movie rating.

# If age < 13, suggest "PG"
# If 13 <= age < 18, suggest "PG-13"
# If age >= 18, suggest "R"'''
#
# num=int(input('enter your age:-'))
# if num < 13:
#     print(f'{num}PG')
# elif 13 <=num and num < 18:
#     print(f'{num}PG-13')
# else: print(f'{num}R')


'''5.Leap Year Check: Write a Python program to check if a given year is a leap year.
A year is a leap year if:
It is divisible by 4 but not divisible by 100, OR
It is divisible by 400.'''

# num=int(input('enter your year:-'))
# if num%4==0 and num%100!=0:
#     print(f'{num}leap_year')
# else: print('not leap_year')
# or
# num=int(input('enter your year:-'))
# if (num%400==0) or (num%4==0 and num%100!=0):
#     print(f'{num}leap_year')
# else: print('not leap_year')


'''6.Maximum of Three Numbers: Write a program to find the largest of three numbers entered by the user using 
if-elif-else.
'''
# li=[a,b,c]---------------edit
# for i in li:
#     if i<=i+1:
# print (b is grater)





'''7. Calculator: Write a simple calculator programme that takes two numbers and an operation (+, -, *, /) 
as input and prints the result. Use if-elif statements to handle the different operations.
'''
# num1 =num (input('enter your first number:-'))------------edit
# num2 =num (input('enter your second number:-'))
#
# if num=='+':
#     print(('num1'+'num2'=='num1'+'num2'))
# # elif num=='-':
#     print(('num1'-'num2'=='num1'-'num2'))
# elif num=='*':
#     print(('num1'*'num2'=='num1'*'num2'))
# else: print(('num1'%'num2'=='num1'%'num2'))






'''8.BMI Calculator: Write a program that calculates a user's BMI and categorizes it based on the result:

# BMI < 18.5: Underweight
# 18.5 <= BMI < 24.9: Normal weight
# 25 <= BMI < 29.9: Overweight
# BMI >= 30: Obese
# '''
# num=float(input('enter your BMI:-'))
# if num< 18.5:
#     print(f'{num}Underweight')
# elif 18.5 <= num and num< 24.9:
#     print(f'{num} Normal weight')
# elif 25 <= num and num < 29.9:
#     print(f'{num} Overweight')
# else: print(f'{num} Obese')


'''9.Traffic Light Simulation: Simulate a traffic light. Ask the user to input a color 
("red", "yellow", or "green"), and based on the input, print the action.

Red: Stop
Yellow: Slow down
Green: Go
'''
# st=str(input('enter your colour:-'))
# if st=='Red':
#     print(f'{st} Stop')
# elif st=='Yellow':
#     print(f'{st} Slow down')
# else: print(f'{st} Go')


'''10.Vowel or Consonant: Write a Python program that checks if a given letter is a vowel (a, e, i, o, u) 
or a consonant.'''
# st=str(input('enter your letter:-'))
# if st=='a'or st=='e'or st=='i'or st=='o'or st=='u':
#     print(f'{st} Vowel')
# else: print(f'{st} consonant')


'''22--------10-----------2024'''
# Python program to count number of vowels using sets in given string
# Python ! ways to count number of sub-string in  string
# Python !
# Python !
# Python !

# st='DO I jjfyf $56456 %%$$$%$%'
# di={}
# for i in di():
#     if i.isdigit:
#         print(di)
#     else:
#         di[i]
# =1for k,v in items()
# print(di.items()):

'''write a Python program to swap the first and last element of the list using Python.'''
# list= [1, 2, 3, 4, 5]
# list[0],list[-1]=list[-1],list[0]
# print(list)


'''Find the length of the list and simply swap the first element with (n-1)th element.'''
# def swapList(newList):
#     size = len(newList)
#     # Swapping
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp
#     return newList
# # Driver code
# newList = [12, 35, 9, 56, 24]
#
# print(swapList(newList))


'''Swapping first and last items in a list using tuple variable'''

# def swapList(list):
#     list[-1], list[0]=list[0], list[-1]
#     return list
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))


'''How to Add Two Numbers in Python'''

# a=6
# b=8
# sum=a+b
# # print(sum)
# print(f'sum of {a} and {b} is sum is :{sum}')

'''Add Two Numbers with User Input'''
# var(input('enter your num:-')):
# num(input('enter your num2:-')):
# sum=int(num1)+int(num2)
#
# print(sum)

