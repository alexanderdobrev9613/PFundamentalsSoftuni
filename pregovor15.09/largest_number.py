number = int(input())

# Create a list to store the digits
digits = []

# Extract and store each digit
while number > 0:
    digit = number % 10
    digits.append(digit)
    number //= 10

# Sort the digits in descending order
digits.sort(reverse=False)

# Calculate the largest number
largest_number = 0
for digit in digits:
    largest_number = largest_number * 10 + digit

# Print the largest number
print(largest_number)