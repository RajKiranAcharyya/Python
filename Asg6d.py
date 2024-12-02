str1 = input("Enter A string: ")
slice_position=(input("Enter The Starting Slicing Position: "))
index=slice_position.split(" ")
sliced=str1[(int(index[0])) : (int(index[1])+1)]
print(sliced)        #radar
if sliced == sliced[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
#A synthetic aperature radar can detect the presence of water and ice.