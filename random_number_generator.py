import random

def generate_random_number():
    return random.randint(1, 100)  # Generates a random integer between 1 and 100

if __name__ == "__main__":
    random_number = generate_random_number()
    print("Random number:", random_number)
