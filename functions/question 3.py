#calculating the factorial of a number.
def factorial_number(p):
    if p == 0:
        return 1
    else:
        return p * factorial_number(p-1)
p=int(input("Input a number to compute the factiorial_number : "))
print(factorial_number(p))