# Binary Code Exercise
a = 0b10111011
x = a>>3
print(bin(x))
# Arithmetic Operations Exercise 2
import math
Basic_Salary = int(1500)
Bonus_Rate = int(200)
Commision_Rate = float(0.02)
Laptop_Quantity = int(input("Enter number of laptops\n"))
Laptop_Price = int(input("Enter price of a laptop R\n"))

Bonus = (Bonus_Rate * Laptop_Quantity)
Commision = (Commision_Rate * Laptop_Quantity * Laptop_Price)
Gross_Salary = (Basic_Salary + Bonus + Commision)
if Laptop_Price < Bonus:
    print("Error")
else:
    print(Gross_Salary)