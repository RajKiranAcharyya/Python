n=int(input("Enter The No. Of Rows: "))
i=1
for i in range (n+1):
    for j in range(n-i):
        if(j == 0 or j== n-1):
            print(" ",end="")
    for k in range(2*i-1):
        if(k == 0 or k== 2*i-1):
            print("*",end="")
    print(end="\n")
# for i in range(n-1,0,-1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i-1),end="")
#     print(end="\n")