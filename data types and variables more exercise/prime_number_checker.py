n = int(input())
is_prime = False

if n <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            print(is_prime)
            break
if is_prime == True:
    print(is_prime)

