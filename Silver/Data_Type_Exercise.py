Numbers = [56,78,34,21,56,34,125,45,89,75,12,56]
print(type(Numbers))
print(sum(Numbers))
Numbers.sort() # Arrange numbers in ascending order. Easier to find largest and smallest numbers in the list
print("Smallest Number is:", Numbers[0])
print("Largest Number is:", Numbers[11])
true_list = list(set(Numbers))
print(true_list)

