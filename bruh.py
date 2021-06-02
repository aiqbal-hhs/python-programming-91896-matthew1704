number = int(input("Pick a number: "))

if number <= 10:
  print("That's a small number!")
elif number > 10 and number <= 100:
  print("That's a medium sized number")
elif number > 0:
    print("hey that number is too low")
else:
  print("Wow that's massive!")
