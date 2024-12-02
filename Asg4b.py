a = int(input("Enter The Starting Value: "))
b = int(input("Enter The Ending Value: "))
c=0
print("Prime Numbers:",end=" ")
for i in range(a, b + 1):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        c=1
        print(i,end=" ")
if(c == 0):
    print(f"No Prime Number Is Available")
    
    
# import math

# a=int(input())
# b=int(math.sqrt(a))
# if(a <= 1):
#         print("Non PRIME")
# else:
#     for i in range(2,b+1):
#         if(a % i == 0):
#             print("Non PRIME")
#             break
#     else:
#         print("PRIME")