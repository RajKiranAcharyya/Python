num1=eval(input("Enter 1st Number: "))
num2=eval(input("Enter 2nd Number: "))
print(f"Using Third Variable\nBefore Swapping num1={num1} and num2={num2}")
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print(f"After Swapping num1={num1} and num2={num2}")


num3=eval(input("\nEnter 1st Number: "))
num4=eval(input("Enter 2nd Number: "))
print(f"Using XOR \nBefore Swapping num1={num3} and num2={num4}")
num5 = num3
num3 = num4
num4 = num5
print(f"After Swapping num1={num3} and num2={num4}")


num6=eval(input("\nEnter 1st Number: "))
num7=eval(input("Enter 2nd Number: "))
print(f"Using TUPPLE \nBefore Swapping num1={num6} and num2={num7}")
num6,num7=num7,num6
print(f"After Swapping num1={num6} and num2={num7}")