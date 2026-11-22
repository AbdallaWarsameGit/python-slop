gryffindor = 0
ravenclaw = 0 
hufflepuff = 0
slytherin = 0

answer = int(input("Do you like (1) dawn or (2) Dusk"))
if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print(" Wrong input try again")

answer = int(input("When Im dead I want people to remember me as: (1) The good (2) The great (3) The wise (4) The bold"))
if answer == 1:
  hufflepuff += 2
elif answer ==2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print(" Wrong input")

answer = int(input("Which kind of instrument pleases your ear? (1) The violin (2) The trumpet (3) The piano (4) The drum"))
if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print("Wrong input")

print("hufflepuff:", hufflepuff)
print("slytherin:", slytherin)
print("gryffindor:", gryffindor)
print("ravenclaw:", ravenclaw)

if hufflepuff > slytherin and hufflepuff > gryffindor and hufflepuff > ravenclaw:
  print("hufflepuff is your house")
elif slytherin > hufflepuff and slytherin > gryffindor and slytherin > ravenclaw:
  print("Slytherin is your house")
elif ravenclaw > slytherin and ravenclaw > gryffindor and ravenclaw > hufflepuff:
  print ("your house is ravenclaw")
elif gryffindor > slytherin and gryffindor > ravenclaw and gryffindor > hufflepuff:
  print("you house is gryffindor")
else:
  print("its a tie!")