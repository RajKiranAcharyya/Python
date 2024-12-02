a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a == 0:
    print("Invalid Input")
else:
    d = (b**2) - 4 * a * c
    if d == 0:
        r0 = (-b) / (2 * a)
        print(f"Root={r0:.3f}  Roots Are Real And Equal")
    elif d > 0:
        r1 = (-b + d ** (0.5)) / (2 * a)
        r2 = (-b - d ** (0.5)) / (2 * a)
        print(f"Root1={r1:.3f}\nRoot2={r2:.3f}   Roots Are Real And Unequal")
    else:
        r3 = (-b + d ** (0.5)) / (2 * a)
        print(f"Root1={r3:.3f}\nroot2 = {r3.conjugate():.3f} Roots Are Imaginary")
