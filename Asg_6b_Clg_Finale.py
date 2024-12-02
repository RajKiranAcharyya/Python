l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
print(l)
s=[0]*(max(l)+1)
for i in range(len(s)):
    if i in l:
        s[i]=i
print(s)