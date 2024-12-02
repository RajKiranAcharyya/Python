a=int(input("Enter An Integer: "))
for i in range(2,8):
    if(a % i == 0):
        print("Breaked")
        break
else:
    print("Not Breaked")