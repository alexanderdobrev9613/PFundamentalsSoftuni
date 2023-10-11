
def rounded_numbers(input_str):
    numbers = input_str.split()
    rounded_numbers = []
    for num in numbers:
        num = int(round(float(num)))
        rounded_numbers.append(num)

    return rounded_numbers

input_str = input()
print(rounded_numbers(input_str))
