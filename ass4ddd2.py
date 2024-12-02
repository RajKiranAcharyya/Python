n=int(input("Enter The No. Of Rows: "))
for i in range (n):
    if i == n-1:
        print("*"*(2*n-1))
    else:
        print("*"*(i+1))
for i in range (n):
    print(" "*(n+i),end="")
    print("*"*(n-1-i))