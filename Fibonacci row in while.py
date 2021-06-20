#Fibonacci row in while
a = input ()
a = int (a)
i = 2
fib1 = 0
fib2 = 1
print (fib1)
print (fib2)
while i != a : 
    i += 1
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print (fib2)