
def countdown(n):

    print(n)
    if n>0:
       countdown(n-1)
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))



