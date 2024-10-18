# conditional
a=int(input('Enter a number:'))
if a>0:
    print(f'The number {a} is a positive number')
elif a<0:
    print(f'The number {a} is a negative number')
else:
    print("The number is zero")


# Gradeing
score=int(input('Enter score:'))
if score>90:
    print(' your Grade is  A')
elif score<=89 and score>=80:
    print('your Grade is B')
elif score<=79 and score>=70:
    print(' your Grade is  C')
else:
    print('your Grade is D')