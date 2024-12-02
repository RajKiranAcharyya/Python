a = int(input("Enter The No. Of Lines: "))
r = 2 * a - 1
k=0
l=1
for i in range(r):
    if i == (a - 1):
        for j in range(r):
            print("*", end="")
    elif i < (a - 1):
        for j in range(i + 1):
            print("*", end="")
    elif i > (a - 1):
        for j in range(a+k):
            print("", end="")
            k=k+1
        for m in range(a-l):
            print("*", end="")
            l=l-2
    print()