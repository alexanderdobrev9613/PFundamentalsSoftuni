version = [int(digit) for digit in input().split('.')]
version[-1] += 1

#[3,9,9]

for index in range(len(version) -1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index-1] += 1

print(".".join(str(number) for number in version))