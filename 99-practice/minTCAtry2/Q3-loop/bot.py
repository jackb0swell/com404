#ask user for miles
print("How many miles must I travel before I reach the secret base?")
miles_to_base=int(input ())
print("I will count the miles...")

#display countdown
print()

for count in range(miles_to_base, 0, -1):
    print("I have", count, "miles to go before I reach the base")

print("I have arrived at the secret headquarters of the MIB!")
print("It's time to sneak in")


