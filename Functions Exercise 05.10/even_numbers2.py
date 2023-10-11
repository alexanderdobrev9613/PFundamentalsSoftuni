def is_even(number):
    if number % 2 == 0:
        return True
    return False



numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
result = []
for element in numbers_as_digits:
    if is_even(element): #if is_even(element) == True
        result.append(element)
print(result)