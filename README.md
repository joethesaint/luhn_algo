# Luhn Algorithm

The Luhn Algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate various identification numbers, most commonly credit card numbers. It helps to quickly detect accidental errors when inputting or transmitting the number.

This repository contains a Python implementation of the Luhn Algorithm along with an example of how to use it.

## Usage

1. Clone the repository to your local machine using:

   ```bash
   git clone https://github.com/joethesaint/luhn_algorithm.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd luhn_algorithm
   ```

3. Open your Python interpreter or a script and import the `luhn_algorithm` function:

   ```python
   from luhn_algorithm import luhn_algorithm
   ```

4. Use the `luhn_algorithm` function to validate a card number:

   ```python
   card_number = "5490 1234 5678 9123"
   is_valid = luhn_algorithm(card_number)
   print(is_valid)  # Output: False
   ```

   Replace the `card_number` with the credit card number you want to validate.

## How the Luhn Algorithm Works

The Luhn Algorithm follows these steps to validate a credit card number:

1. Reverse the card number and convert it to a list of integers.
2. Double the value of every odd-indexed digit (1-indexed).
3. If the doubled digit is greater than 9, subtract 9 from it.
4. Sum all the digits.
5. If the total sum ends in 0 (i.e., is divisible by 10), the card number is valid.

## Contributing

If you find any issues with the implementation or have suggestions for improvements, feel free to open an issue or submit a pull request. Your contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
