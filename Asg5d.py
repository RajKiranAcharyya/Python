a = input("Enter A Statement: ")
b = (int(input("Enter The 1st Specifed Index: "))) - 1
c = (int(input("Enter The 2nd Specifed Index: "))) - 1
i = b
d = (b + c) // 2
COPYc=c
while i <= d:
    if a[i] == a[c]:
        c = c - 1
        i = i + 1
    else:
        print("Not Palindrome")
        break
if i == d + 1:
    print(a[b:(COPYc)+1],"\nPalindrome")