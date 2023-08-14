def luhn_algorithm(card_number):
    # reverse card number and convert to list of integers
    digits = [int(digit) for digit in reversed(card_number.replace(" ",""))]

    # double the value of every odd-indexed digit
    doubled_digits = [digit * 2 if idx % 2 == 1 else digit for idx, digit in enumerate(digits)]

    # when a digit is greater than 9, subtract 9 from it
    processed_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]

    # sum all the digits
    total = sum(processed_digits)

    # check if the total ends in 0
    return total % 10 == 0

# Test example
mastercard_number = "5490 1234 5678 9123"
is_valid = luhn_algorithm(mastercard_number)
print(is_valid) # Output: False

