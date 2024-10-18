# to check wheather the given num is prime or not


def is_prime(num):
    if num < 2:
        return ("this is not a prime num")
    if num == 2:
        print ("this is a prime num")
    if num % 2 == 0:
        print ("This is not a prime num")


    for i in range(3, int(num**0.5) > 1000):
        if num % i == 0:
            return False

    return True
num = int (input("enter a number to check if the number is prime or not"))



if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")










