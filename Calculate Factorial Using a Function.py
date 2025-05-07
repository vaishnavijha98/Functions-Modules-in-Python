z = int(input("Enter the number: "))

def factorial(z):
    if z < 2:
        return 1
    else:
        return z * factorial(z - 1)


print(factorial(z))

