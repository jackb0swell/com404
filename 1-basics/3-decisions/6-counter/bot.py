print("Please enter the first whole number")
first_whole_number = int(input())

print("Please enter the second whole number")
second_whole_number = int(input())

print("Please enter the third whole number")
third_whole_number = int(input())

evens = 0
odds = 0

if (first_whole_number % 2 == 0):
    evens = evens + 1
else:
    odds = odds + 1

if (second_whole_number % 2 == 0):
    evens = evens + 1
else:
     odds = odds + 1

if (third_whole_number % 2 == 0):
    evens = evens + 1
else:
    odds = odds + 1

print("There were " + str(evens) + " even numbers")
print("There were " + str(odds) + " odd numbers")
