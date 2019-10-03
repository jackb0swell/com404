print("Please enter the first number")
first_number = int(input())

print("Please enter the second number")
second_number = int(input())

if first_number > second_number:
    print("The second number is smallest")

elif second_number > first_number:
    print("The first number is smallest")

elif first_number == second_number:
    print("Both numbers are the same!")
