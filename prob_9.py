def prob_9():
  # Problem 9: Password Strength Checker
  password = input("Type Password: ") #input that will ask the user to input a password
  pass_length = len(password) #this will check the length of the password
  if pass_length < 6: #if the password is less than 6 characters it will print out the following
    print("Password is too short")
  elif password.isdigit(): #if the password is a number it will print out the following
    print("Weak Password")
  elif password.isalpha(): #if the password is a letter it will print out the following
    print("Moderate Password")
  else: 
    print("Strong Password")