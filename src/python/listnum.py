# Create a list of the given numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 1, 3, 5, 2, 5, 1]

print(numbers)
# appending
inputnum= 7
numbers.append(inputnum)
print(numbers)
#removing num from list

remove= numbers.pop(1)
print(numbers)

#descending order

sorted_numbers = sorted(numbers, reverse=True)

print(sorted_numbers)
