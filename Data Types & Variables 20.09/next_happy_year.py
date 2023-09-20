year = int(input())
year_is_special = False

while not year_is_special: #dokato ne e True
    year += 1
    year_as_string = str(year)
    year_is_special = True
    for digit in year_as_string:
        if year_as_string.count(digit) > 1: #ako ima povtorenie
            year_is_special = False
            break
print(year)