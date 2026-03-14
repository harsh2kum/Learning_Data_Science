## Processes that runs in parallel are called Multiprocessing

# When to use multiprocessing --> CPU-Bound Tasks that are heavy on CPU usage (eg. mathematical computations, Data Processing).

# Parallel Execution - Multiple cores of thr CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square: {i*i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube: {i * i * i}')

if __name__ == "__main__":

    # Create 2 processes

    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start = time.time()

    # Start the process 
    p1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    print("Finished in:", time.time() - start)
