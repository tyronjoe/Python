Number = 1
while Number < 11:
    print(Number)
    Number += 1

Number = 100  # Loop starting point
while Number >= 2:  # Loop ending point
    print(Number)  # Print numbers from 100 to 2
    Number -=2  # Loop moves in a decreasing order, starting loop -2 until ending loop

Number = int(input("Enter Number\n"))
for i in range(1, 11):  # User input multiplied by numbers between 1 and 11
    print(Number, 'x', i, '=' , Number * i )  # Print answers in multiplication table form
