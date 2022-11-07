def username_generator(first, last):
  return first[0:3] + last[0:3]

def password_creator():
  while True:
    pword = input("Input password, it must be longer than 6 characters, be a mixture of upper and lower case, contain a number or symbol, contain a letter: ")
    if len(pword) < 6:
      print("Password is too short, please try again.")
    elif pword.isnumeric():
      print("Password must contain a letter, please try again.")
    elif pword.isalpha():
      print("Password must contain a number or symbol, please try again.")
    elif pword == pword.lower() or pword == pword.upper():
      print("Password must be a combination of upper and lowercase, please try again.")
    else:
      print("Password accepted.")
      return pword

def store_details(fname, lname, uname, pword):
  userdetails = {}
  userdetails["First Name"] = fname
  userdetails["Last Name"] = lname 
  userdetails["User Name"] = uname 
  userdetails["Password"] = pword 
  return userdetails

def login(user_details, attempts):
  if attempts == 3:
    print("Login attempts exceeded.")
    return
  else:
    username_given = input("Input your username: ")
    password_given = input("Input your password: ")
    if username_given == user_details["User Name"] and password_given == user_details["Password"]:
      print("Login successful.")
      return
    else:
      print("Login Failed, please try again.")
      login(user_details, attempts + 1)
  
first_name = input("What is your first name? ").title()
last_name = input("What is your surname? ").title()
user_name = username_generator(first_name, last_name)
password = password_creator()
user_details = store_details(first_name, last_name, user_name, password)
attempts = 0
login(user_details, attempts)