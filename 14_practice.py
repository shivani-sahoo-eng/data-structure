# def is_armstrong(num):
#     str_num=str(num)
#     length_of_num=len(str_num)
#     sum=0
#     for i in str_num:
#
#         cube=int(i)**length_of_num
#         sum=sum+cube
#         return sum==num

# for i in range(100,1001):
#     if is_armstrong(i):
#         print(i)
#
#
#
#     def is_even-odd(num):
#         if num%==0:
#             print('even')
#             length_of_num = len(str_num)
#                 sum=0
#                 for i in str_num:
#
#                     cube=int(i)**length_of_num
#                     sum=sum+cube
#             if sum==num:
#                 return num,'is armstrong and even'
#         else:
#
#             def is pallindrom(num):
#
# length_of_num=len(str_num)
#     sum=0
#     for i in str_num:
#
#         cube=int(i)**length_of_num
#         sum=sum+cube
#         return sum==num


'''decorator-outside function,its take argument as a exiting  function name and
modify the exiting functionality and add the new functionality of the exiting
function,
return extensible functionality of a exting function
create the relationship between decorator and exiting function using @ symbol,
write the decortor name help of @ above of the exiting function
'''

# n=123
# reverse_num=0
# while n!=0:
#     reminder = n%0
#     print(remindere)


# def is_pallindrom(n):
#     n=num
#     reserved_num=0
#     while n !=0:
#         reminder = n % 10
#         reversed_num= reserved_num *10 + reminder
#         n=n//10
#     return num== reversed_num,reversed_num
# print(is_pallindrom(121))





# decorator chaining--

# def f():
#     for i in range(1,10):
#         return i
# print(f())
# funtion return only one time

# generator is a function who generate the data one by one using yield keyword, instead of return here

# write a forloop in afunction range(1,6),and exponent each element in cub
# def 1():
# for i in range(1,6):
#     yield i**3
#
# var= f1()
# for i in range(5):
#     print (next(var))

# st = 'aaabbccddecd' --- i want to calculate occurance each char.
#                     {a:3,b:2,c:3,d:3,e:1}
# # st = 'aabaabbaa' {a:2,b:1.a:2,b:2,a:2}

# st='aaabbccddecd'
# a={}
# b={}
# c={}
# d={}
# for i in st:
#     i== i.count():
# print(st)
#


# st='ABCD'
# n=len(st)
# di={}
# for i in range(n):
#     di[st[i]]=i
# print(di)

'''for i in range(1,6):
    for j in range(1,6):
        print(i,j)'''

# for i in range(1,6):
#     print('*'*i)

# for i in range(1,6):
#     print('*'*(6-i))
#
# for i in range(1,4):
#     print('*'*i)
# for i in range(1,3):
#     print('*'*(3-i))


# *****
#  ****
#   ***
#    **
#     *

# for i in range(5):
#     print(' '*i, '*'*(5-i))


# for i in range(1,6):
#     print(' '* (i-1),'*'*(6-i))


# li=[10,67,32,24,56,21,68,31]
# # op=[10,21,24,31,32,56,67,68]
#
# n=len(li)
# for i in range(n):
#     for j in range (0,n-i-1):
#         if li[j]>li[]

# li=[1,[2,[3,[4,[5,[6,[7,[8,[9,[10]]]]]]]]]]

# li=[1,2,3,[4,5,6],[7,8,9]]
# # li=[1,2,3,4,5,6,,7,8,9]
# li1=[]:
# for i in li:
#     if type(i)==list:
#         for j in i:
#         li1.append(j):
#     else:
#         li1.append(i):
# print(li1)

# li=[1,[2,[3,[4,[5,[6,[7,[8,[9,[10]]]]]]]]]]
# def nested_list(li):
#     new_li=[]
#     for i in li:
#         if isinstance(i,list):
#             for j in i:
#                 new_li.extend(nested_list(i))
#         else:
#             new_li.append(i)
#     return new_li
# print(nested_list(li))
#
# # string_prac_all-----line 151,172,165,69,50,phibonasy series,38,count of vowels in a string
# string position change
# special char not change the position only char change position
# dictionary iteration
# how to use if condition in For
# li=[1,2,[3,4],{5,6},(7,8),{'A':9,'B':10}]
# [1,2,3,4,5,6,7,8,9,10]
# LIST=COLLECTION Name Error then iteration

# Nested IF---
# li=[[242,565],777,888,999,[898,676]]
# for i in li:
#     if isinstance (list,i):
#         for j in i:
#             if j % 2:
#                 if str(j)==str(j)[::-1]:
#
#     else:
#         if i%2==0:
#             if str(i)==str(i)[::-1]:
#                 print(i)

# Iterate a Dictionary

# Customers = [
#     {'customer_id':1,'first_name':'John','last_name':'Doe','age':31,'country':'USA'},
#     {'customer_id':2,'first_name':'Robert','last_name':'Luna','age':22,'country':'USA'},
#     {'customer_id':3,'first_name':'David','last_name':'Robinson','age':22,'country':'UK'},
#     {'customer_id':4,'first_name':'John','last_name':'Reinhardt','age':25,'country':'UK'},
#     {'customer_id':5,'first_name':'Betty','last_name':'Doe','age':28,'country':'UE'}
# ]

# for var in customers:
#     if var['customers']>=5,
#         print(var['customers'])

# Customers = [
#     {'customer_id':1,'first_name':'John','last_name':'Doe','age':31,'country':'USA','subject':['Python','Java','C++']},
#     {'customer_id':2,'first_name':'Robert','last_name':'Luna','age':22,'country':'USA','subject':['Goloang','R','C++']},
#     {'customer_id':3,'first_name':'David','last_name':'Robinson','age':22,'country':'UK','subject':['Python','Java','SQL']},
#     {'customer_id':4,'first_name':'John','last_name':'Reinhardt','age':25,'country':'UK','subject':['Java','C++']},
#     {'customer_id':5,'first_name':'Betty','last_name':'Doe','age':28,'country':'UE','subject':['Python','Perl']}
# ]
#
# Orders = [
#     {'order_id':1,'item':'keyborad','amount':400,'customer_id':4},
#     {'order_id':2,'item':'Mouse','amount':300,'customer_id':4},
#     {'order_id':3,'item':'monitor','amount':12000,'customer_id':3},
#     {'order_id':4,'item':'keyborad','amount':400,'customer_id':1},
#     {'order_id':5,'item':'MousePad','amount':250,'customer_id':2},]
#
# amount_li=[]
# for i in Orders:
#     amount_li.append(i['amount'])
# max_amount=max(amount_li)
#
# cst_id=None
# for j in Orders:
#


'''Customers_data = { 'data':
    [{'customer_id':1,'first_name':'John','last_name':'Doe','age':31,'country':'USA'},
    {'customer_id':2,'first_name':'Robert','last_name':'Luna','age':22,'country':'USA'},
    {'customer_id':3,'first_name':'David','last_name':'Robinson','age':22,'country':'UK'},
    {'customer_id':4,'first_name':'John','last_name':'Reinhardt','age':25,'country':'UK'},
    {'customer_id':5,'first_name':'Betty','last_name':'Doe','age':28,'country':'UE'}]
}
'''
# for i in Customers_data['data']:
#     if i['country']=='USA':
#         print(i['first_name'])





data = {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": "https://reqres.in/img/faces/7-image.jpg"
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": "https://reqres.in/img/faces/8-image.jpg"
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": "https://reqres.in/img/faces/9-image.jpg"
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": "https://reqres.in/img/faces/10-image.jpg"
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": "https://reqres.in/img/faces/11-image.jpg"
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": "https://reqres.in/img/faces/12-image.jpg"
        }
    ],
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

# for key,value in data items():
#     print(value)

# for i in data['data']:
#     print (i['email'])

# st=''
# for i in data['data']:
#     email=i['email']
#     first_str=email.split('.')[0]
#     st = st+' '+first_str
# print(st)


# st=''
# for i in data['data']:
#     email=i['email']
#     sec_str=email.split('.')[1]
#     last_name=sec_str_s

# for i in data['data']:
#     print(len(i))


# conditional iteration
# while loop

# while condition:
#     statement

# count= 1
# while count <=10:
#     print(count)
#     count=count+1


# count= 1
# while count <=10:
#     if count%3==0:
#         count = count + 1
#         continue
#     print(count)
#     count=count+1

# count=1
# sum=0
# while count<=20:
#     if count%4==0:
#         sum = sum + count
#     count=count+1
# print(sum)

# print(ord('A'))
# print(ord('A'))

# char_code=ord('A')
# while char_code<=ord('Z')
# char_code=char_+1


# char_code=ord('A')
# while char_code<=ord('Z'):
#     print(chr(char_code))
#     char_code=char_code+1


# assicc char count

# char_code=ord('A')
# while char_code<=ord('Z'):
#     vowels='AEIOU'
#     if chr(char_code) in vowels:
#         char_code = char_code + 1
#         continue
#     print(chr(char_code))
#     char_code=char_code+1


# a=0#3
# b=1#5
# while a<=30:
#     print(a)#0,1,2,3
#     a,b=b,a+b

# lambda
# list comprehension
# interpretor compiler
# operator

'''22---10-------2024'''


















