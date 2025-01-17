
print("Welcome to the tip calculator")
total_bill = int(input("What was the total bill: $"))
tip = int(input("How much tip would you like to give? 10%, 12% or 15%? "))
persons = int(input("How many people to split the bill: "))

payment_per_person =  (total_bill * (1 + tip / 100)) / persons

print(f"Each person should pay {round(payment_per_person, 2)}")