# x=10
# print(type(x))    #<class 'int'>

# y=11.5
# print(type(y))    #<class 'float'>

# z=complex(2,3)
# print(type(z))   #<class 'complex'>

# s='Hello'
# print(type(s))  #<class 'str'>

# l=[1,2,3]
# print(type(l))   #<class 'list'>

# t=(1,2,3)
# print(type(t))   #<class 'tuple'>

# b=True
# print(type(b))   #<class 'bool'>

# a=10  
# print(id(a))    #1940218456     //id is not memory address,it is a reference of value

# b=5
# print(id(b))    #1940218376

# c=10
# print(id(c))  #1940218456

# c=5
# print(id(c))   #1940218376       mutable__It can be changed

# s="Hello"
# print(s[0])        # H

# #s[0]="h"
# #print(s)         #Error     immutable__It can not be changed

# s="hello"
# print(s)          #hello     string is not changes directly,the reference is changed.


# # mutable objects list,tupple,set 
# # immutable objects string,tupple

# a=10
# b=5
# c=a+b
# print(c)  #15
# print("The Addition Is",c)  #The Addition Is 15
# print(a,"+",b,"=",c)         #10 + 5 = 15

# print("Hello")   #Hello
# print("World")   #World

# print("Hello",end=" ")   
# print("World")            #Hello World


# print("Hello","World")  #Hello World


# print("Hello","World",sep=",")   #Hello,World       Separator


# print("Hello","World",end=",")   #Hello World,   //end means ENDING with the symbol



# a=10
# b=5
# print(f"a={a} and b={b}")   #a=10 and b=5

# print(f"{a} + {b} = {a+b}")    #10 + 5 = 15

# pi=3.1415692
# print(f"pi={pi:0.2f}")   #pi=3.14

# p=123456789
# print(f"Currency={p:,}")   #Currency=123,456,789

# p=123456789.2596
# print(f"Currency={p:,.2f}")    #Currency=123,456,789.26


x=eval(input("Enter A Number"))    #After Inputting no.,the fuction will return str 5,so it will be concatinated.







