a1 = 5
a2 = 11
match a1:
    case 1:
        print(1)
    case _ if (a2 > 10):
        print(2)
    case _:
        print("Bye")

# # x=3+5j
# # print(type(x))  #<class 'complex'>

# # x=complex(3,5)
# # print(x)  #(3+5j)

y = complex(3.5, 0.67)
# print(y)               #(3.5+0.67j)

# print(y.real)                #3.5
# print(y.imag)       #0.67

print(y.conjugate())  # (3.5-0.67j)
