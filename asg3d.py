# v=(input("Enter A Character: "))
# match v:
#     case 'A' |'a':print(f"The Input '{v}' is Vowel") 
#     case 'E' |'e':print(f"The Input '{v}' is Vowel")
#     case 'I' |'i':print(f"The Input '{v}' is Vowel")
#     case 'O' |'o':print(f"The Input '{v}' is Vowel")
#     case 'U' |'u':print(f"The Input '{v}' is Vowel")
#     case _ if (v.isalpha() and len(v)) == 1:print(f"The Input '{v}' is Consonant")
#     case _: print(f"The Input '{v}' is Invalid")



v=(input("Enter A Character: "))
match v:
    case ('A' |'a') | ('E' |'e')| ('I' |'i') | ('O' |'o') | ('U' |'u'):print(f"The Input '{v}' is Vowel") 
    case _ if (v.isalpha() and len(v) == 1):print(f"The Input '{v}' is Consonant")
    case _: print("Invalid Input")