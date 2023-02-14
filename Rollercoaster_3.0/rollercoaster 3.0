print("Welcome to rollercoaster!")

height = int(input("What is your height in cm?"))
bill = 0 

if height >= 60:
  print("You can ride the rollercoaster!")

  age = int(input("Please enter your age: "))
  if age < 12:
    bill += 50
    print("Entry fee is 50sek")
  elif age == 18:
   bill += 70
   print("Entry fee is 70sek")
  elif age > 45 and age < 55:
   bill += 0
   print("You can enter for free")
  else:
   bill += 100
   print("Entry fee is 100sek")
  
  photo = input("Would you like to get your picture printed?(Y / N)")
  if photo == "Y":
    bill += 3
  else:
    print("Please proceed to the entrace!")

    print(f"You final bill is {bill} SEK")

else:
 print("Sorry, you need to be higher than 60cm =(")
