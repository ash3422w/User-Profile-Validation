name = input("Enter your full name: ")
email = input("Enter your email id: ")
s = input("Enter your mobile number: ")
age = int(input("Enter your age: "))
count = False
if name.count(" ") >= 1 and name[0] != " " and name[-1] != " ":
   if email.count("@") == 1 and email.count(".") >= 1 and email[0] != "@":
       if len(s) == 10 and s.isdigit() and s[0] != '0':
           if 18 <= age <= 60:
               count = True
if count:
   print("User Profile is VALID")
else:
   print("User Profile is INVALID")
