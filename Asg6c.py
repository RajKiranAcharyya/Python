# str1=input("Enter A string: ")
# upper=0
# lower=0
# for i in str1:
#     if(i >= "A" and i <= "Z"):
#         upper=upper+1
#     if(i >= "a" and i <= "z"):
#         lower=lower+1
# print(upper,lower)

# If lower:: true,,else false
# If upper:: true,,else false

str1 = input("Enter A string: ")
upper = lower = 0
for i in str1:
    if i.isupper():
        upper = upper + 1
    if i.islower():
        lower = lower + 1
print(upper, lower)
