divisor = int(input()) #delitel
boundary = int(input()) #delimo

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break
print(number)