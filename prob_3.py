def prob_3(): 
  # Problem 3: Movie Ticket Price
  age = int(input("What is your age?")) #right here we created a input that allows the user to input their age
  if age < 5:      # we created a if statement that allows us to print out the ticket price for the user if their age is less than 5
    print("Free")  
  elif age >= 5 and age <= 12: #we created a elif statement that allows us to print out the ticket price for the user if their age is between 5 and 12
    print("$8")
  elif age >= 13 and age <=59: # we created a elif statement that allows us to print out the ticket price for the user if their age is between 13 and 59
    print("$12")
  elif age >= 60:
    print("10")
    