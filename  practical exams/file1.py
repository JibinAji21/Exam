# 12. how to remove duplicates in a list using for loop ? 

# l=[1,2,3,3,5,5]
# n=[]
# for i in l:
#     if i not in n:
#         print()
#         n.append(i)
# print(n)


# 13. Create a calculator using function and modules ?

# def numbers():
#     a=int(input("enter first number"))
#     b=int(input("enter second number"))
#     return a,b
# def add():
#     a,b=numbers()
#     print(a+b)
# def sub():
#     a,b=numbers()
#     print(a-b)
# def div():
#     a,b=numbers()
#     print(a/b)
# def mul():
#     a,b=numbers()
#     print(a*b)

# while True:
#     print('''
#           1.Addition
#           2.Substraction
#           3.Division
#           4.Multiplication
#           5.Exit''')
    
#     choice=int(input("enter your choice"))
#     if choice==1:
#         add()
#     elif choice==2:
#         sub()
#     elif choice==3:
#         div()
#     elif choice==4:
#         mul()
#     elif choice==5:
#         break


# 14. Write a python program to print the following pattern ?

# a=65
# for i in range (1,5):
#     for j in range(i):
#         print(chr(a-j),end=" ")
#     print()
#     a+=1
    


# 15. Write a python function to calculate the factorial of a given number?

# def fact():
#     a=int(input("enter a number"))
#     fact=1
#     for i in range(1,a+1):
#         fact*=i
#     print("factorial is,",fact)


# fact()

# 16. Write a python function that takes a dict and returns a new dict with keys and  values swapped?


# method =1


# d={1:'one',2:'two',3:'three'}
# def num(d):
#     d1={}
#     for i in d:
#         d1[d[i]]=i
#     return d1
# print(num(d))


# # output

# {'one': 1, 'two': 2, 'three': 3}


#  method =2

# d={1:'one',2:'two',3:'three'}
# def num(d):
#     return { value:key for key,value in d.items()}
# print(num(d))

# # output

# {'one': 1, 'two': 2, 'three': 3}

