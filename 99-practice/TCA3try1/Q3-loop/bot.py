print("How many heroes must we gather?")

number_of_heroes = int(input())
print("Gathering heroes…")

for count in range(1, number_of_heroes, 1):
    print("…found hero", count)
