numbers = list(map(int, input().split()))
print (numbers)
a = len (numbers)
swip = True
while swip :
    swip = False
    for i in range (a-1):
        if numbers[i] > numbers[i+1] :
            numbers[i] , numbers[i+1] = numbers[i+1] , numbers[i]
            swip = True
print (numbers)