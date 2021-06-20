#Fibonacci row with recursion

def fib (n):
    fib1 = 1
    fib2 = 2
    if n == 1:
        return fib1
    elif n == 2:
        return fib2
    else :
        return fib(n-2) + fib(n-1)

a = int ( input ())
print (fib(a))