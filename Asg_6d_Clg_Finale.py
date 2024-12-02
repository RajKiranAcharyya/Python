a1=input("String: ")
print(a1)
s1=set(a1.split())
d={}
for i in s1:
    d[i]=a1.count(i)
print(d)