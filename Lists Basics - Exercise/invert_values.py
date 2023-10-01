list_with_numbers = input().split() #tuk sa stringove / split deli po interval kato sa prazni skobite, naricha se separator
opposite_numbers = []
for number in list_with_numbers:
    current_number = -int(number)
    opposite_numbers.append(current_number)
print(opposite_numbers)