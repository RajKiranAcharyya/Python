a=eval(input("Enter 1st Number: "))
b=eval(input("Enter 2nd Number: "))
c=eval(input("Enter 3rd Number: "))

print("Max=",end="")
print(a if(a>b and a>c) else (b if(b>c) else c))