number=input("What number do you want to check?")

remainder = int(number) % 2
if remainder == 1:
  print("The number is odd")
else:
  print("The number is even")