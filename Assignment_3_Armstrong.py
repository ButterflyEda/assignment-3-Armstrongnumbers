number = input("Please enter your n-Armstrong number : ")
if number.isnumeric():
  armstrong = 0
  power = len(number)
  for i in number:
    armstrong += int(i)**power
  if armstrong == int(number):
    print(f"{number} is an Armstrong number.")
  else:
    print(f"{number} is not an Armstrong number.")
else:
  print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")