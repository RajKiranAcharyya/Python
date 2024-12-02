n=int(input())
l=[]
for i in range(n):
    l.append(input())
sorted_strings = sorted(l, key=lambda x: x[-1])
# Output the result
print(sorted_strings) 
    