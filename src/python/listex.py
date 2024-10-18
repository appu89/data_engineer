# des n max n min value in list n sum
list = [8, 2, 69, 45, 32, 9, 4, 18]
list.sort(reverse= True)
print(list)
Max=list[0]
print(Max)
Min=list[-1]
print(Min)
print(sum(list))



# string list  n uppercase and joining 
list = ['Windows', 'Linux', 'Mac', 'python', 'MYSQL', 'JavaScript','html']
uppercase = [words.upper() for words in list]
print(uppercase)
largest = max(list)
print(largest)
shortest = min(list)
print(shortest)
join_with = '-'
combined = join_with.join(uppercase)
print(combined)

dict = {'Apoorva' : 98, 'jhanvi' : 92, 'hema' : 75, 'pallavi' : 67, 'megha' : 72, 'vinitha' : 55, 'prem' : 99}
highest = max(dict.values())
lowest = min(dict.values())
for key, val in dict.items():
    if val == highest:
        print(f'{key} has highest score of {val}')
    elif val == lowest:
        print(f'{key} has lowest score of {val}')

dict['prem'] = 99
print(dict)
dict.pop('vinitha')
print(dict)
        
    