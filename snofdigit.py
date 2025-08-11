num = int(input("Enter a number: "))

# Handle negative numbers
num = abs(num)

sum_of_digits = 0

while num > 0:
    sum_of_digits += num % 10   # Get last digit and add to sum
    num //= 10                  # Remove last digit

print("Sum of digits:", sum_of_digits)
