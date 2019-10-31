print("How many zones must I cross?")

number_of_zones = int(input())

print("Crossing zones...")

for count in range(number_of_zones, 0, -1):
    print("…crossed zone", count)

print("Crossed all zones.  Jumanji!")

