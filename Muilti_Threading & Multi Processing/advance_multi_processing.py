from concurrent.futures import ProcessPoolExecutor
import time

# Function to compute square of a number with slight delay
def square_number(number):
    time.sleep(1)  # Simulate work
    return f"Square: {number * number}"

numbers = [1, 2, 3, 4, 5, 7, 8, 9]

if __name__ == '__main__':
    # Create a pool of 3 worker processes
    with ProcessPoolExecutor(max_workers=3) as executor:
        # Map the function to numbers (returns a generator-like object)
        results = executor.map(square_number, numbers)

        # Print the actual results
        for result in results:
            print(result)