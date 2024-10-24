print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
total_tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
percentage = total_tip / 100
print(f"Each person should pay: ${round((total_bill * percentage + total_bill) / people, 2)}")