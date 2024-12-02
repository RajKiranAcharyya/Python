bs=eval(input("Enter The Basic Salary: "))
agp=0.5*bs
print("agp=",agp)
ms=bs+agp
print("ms=",ms)
da=0.5*ms
print("da=",da)
hra=0.15*ms
print("hra=",hra)
print(f"The Total Salary Is: {ms + da + hra:,.2f}")