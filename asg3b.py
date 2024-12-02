y=int(input("Enter A Year: "))
if(y < 1000 or y > 9999):
    print("Invalid Input")
else:
    if((y % 400 == 0) or ((y % 100 != 0) and (y % 4 == 0))):
        print(f"{y} Is A Leap Year")
    else:
        print(f"{y} Is Not A Leap Year")