#task with factorial
print ("Enter the number")
f = input()
print("Your number for factorial -", f)
f = int (f)
n = f - 1
while n >= 1 :
    f = f * n
    n -= 1
print ("The answer is -", f)