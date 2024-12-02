a=int(input("Enter An Integer(Min Three Digit): "))
while(a > 100):
    a = a//10
if(a % 7 == 0):
    print("Divided By 7")
else:
    print("Not Divided By 7")

i=1
while(i<10):
    print(i)
    i=i+1    #1 to 9

i=1
while(i<10):
    print(i)
i=i+1         #Infinite

l=range(1,5)
print(l)    #range(1, 5)

print(type(l))   #<class 'range'>

print(list(l))  #[1, 2, 3, 4]

print(*l)   #1 2 3 4

# * is meant by unpacking operator

l1=[1,2,3,4,5]
print(l1)       #[1, 2, 3, 4, 5]
print(*l1)   #1 2 3 4 5

l2=range(1,5,2)
print(*l2)       #1 3


l3=range(9,0,-2)
print(list(l3))

for i in range(100,1000):
    print(i)

a=int(input("Enter An Integer: "))
b=a**2
while(b >100):
    b = b - 100
if(a == b):
    print("Automorphic")


a=int(input("Enter An Integer: "))
for i in range(2,round((a**0.5)+1)):
#     if(a == 0):
#         print(f"{a} Is Not A Prime Number ")
#         break
    if(a % i == 0):
        print(f"{a} Is Not A Prime Number ")
        break
else:
    print(f"{a} Is A Prime Number ")
