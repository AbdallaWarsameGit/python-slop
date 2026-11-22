Hight = int(input("Enter your hight"))
Cost = int(input("Please enter 10 credits"))
if Hight >= 137 and Cost >= 10:
  print("Enjoy the ride!")
elif Hight < 137 and Cost >= 10:
    print("You are not tall enough to ride")
elif Hight >= 137 and Cost < 10:
  print ("You do not have enough credits")
elif Hight < 137 and Cost < 10:
  print("sorry you have not met either requirement")