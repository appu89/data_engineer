# craete 2 sets union, intersection, difference and symmetric difference
s1= {3,6,9,5,1,2}

s2= {2,4,6,10,8,5}

print("Union of elements: ", s1 | s2)
print("Intersection of elements: ", s1 & s2)
print("Difference of elements: ", s1 - s2)
print("Symmetric Difference of elements: ", s1 ^ s2)


# l, remove duplicates, add new eleemnt, remove an existing element
l = ['Apoorva', 'priya', 'prem', 'ajay', 'srikanth', 'ajay', 'sai']
s = set(l)
print("Elements after removing duplication: ",s)

l.append('naveen')
print(l)

l.pop(5)
print(l)