# Random Number Generator

This Python script generates a random number between 1 and 100 using Python's `random` module.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the `random_number_generator.py` file.
3. Run the script using Python:

```bash
python random_number_generator.py



### Explanation:

The provided Python script does the following:

1. It imports the `random` module, which provides functions for generating random numbers.
2. It defines a function `generate_random_number()` which does the following:
   - Uses `random.randint(1, 100)` to generate a random integer between 1 and 100.
   - Returns the generated random number.
3. It includes a check `if __name__ == "__main__":` to ensure that the following code block is only executed when the script is run directly, not when it's imported as a module into another script.
4. Inside the `if` block, it calls the `generate_random_number()` function to generate a random number and assigns it to the variable `random_number`.
5. It prints the generated random number to the console using `print("Random number:", random_number)`.

This script is a simple demonstration of how to generate random numbers in Python using the `random` module.

