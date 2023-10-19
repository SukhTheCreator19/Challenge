def prob_6():
  # Problem 6: Weekend or Weekday
  # This code asks the user the day of the week and checks wether it is a weekday, the weekend or not a day at all 
  day = input("What day is it? ")
  if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
  elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("It's a weekday!")
  else:
    print("That's not a day!")
