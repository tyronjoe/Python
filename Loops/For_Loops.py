Cars = ["BMW", "VW", "FORD", "Subaru", "Nissan", "McLaren", "Lamborghini", "Pagani", "Bugatti"]
Food = ["Chicken", "Beef", "Vegetables", "Sauce", "Fruit"]
for vehicles in Cars:
    for produce in Food:
        print(vehicles, produce)

for num in range(1, 11):
    print(num)  # Displaying numbers 1 to 10

for num in range(2, 22, 2):
    print(num)  # Displaying numbers 2 to 20 via +2
else:
    print("I'm done with 'for' loops")

# Task 2
k = 1
for i in range(0, 4):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()

# Exercise 1
for num in range(1, 100):  # Display numbers 1 to 100
    if num % 3 == 0 and num % 5 == 0:  # If number is divisible by both 3 and 5
        print("FizzBuzz")  # display 'FizzBuzz' instead of the number
    elif num % 3 == 0:  # If number is divisible by 3
        print("Fizz")  # display 'Fizz' instead of the number
    elif num % 5 == 0:  # If number is divisible by 5
        print("Buzz")  # display 'Buzz' instead of the number
    else:  # All the above requirements not met
        print(num)  # display number