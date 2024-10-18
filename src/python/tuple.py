# create tuple ,last 4 elements,repeated elements,adding to tuple ,converting to list
t = (25, 9.2, 54, 7.5, 3.67, True, "welcome", False, "learning", "Python3")
x = t[1]  
print(x)

y = t[-4:]
print(y)

index_value = t.index(3.67)
print(index_value)


count_value = t.count(25)
print(count_value)

a = t + (36, 92)
print(a)
x = list(t)
x.extend([45, 88]) 
y = tuple(x)
print(y)

x = list(t)
x.remove(25)  
y = tuple(x)
print(y)


# packing n Unpacking
pt= "appu",8,False
print(pt)
a, b, c= pt
print(a)
print(b)
print(c)