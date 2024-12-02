n=int(input("Enter The No. Of Rows: "))
i=1
for i in range (n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print(end="\n")

for i in range(n-1,0,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print(end="\n")