print("How many miles must I travel before I reach the secret base?")
number_of_miles = int(input ())

print("I will count the miles...")

print()

for count in range(number_of_miles, 0, -1):
    print("I have", count, "miles to go before I reach the base")

print("I have arrived at the secret headquarters of the MIB!")
print("It's time to sneak in")