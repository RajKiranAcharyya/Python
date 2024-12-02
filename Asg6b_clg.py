email = input("Enter Your Email-ID:")
# print(email)                11600223077@mckvie.edu.in
roll = email.split("@")
# print(roll)                       #['11600223077', 'mckvie.edu.in']       #list data type
print(roll[0], end=" ")
domain = roll[1].split(".")
# print(domain[1])                edu
print(domain[0].upper())  # 1160022377 MCKVIE
