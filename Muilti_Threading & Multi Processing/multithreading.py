### Multithreading 
### When to use Multi Threading 
# I/O - Bound Tasks: Tasks thst spend more time waiting for I/O operation(eg: File Operation, Network Requests).
#  Concurrent execution: When you want to improve the throughput of your application by Performing multiple Operations Concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f'Number:{i}')

def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}')

# Create 2 Threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()

# Start the thread 
t1.start()
t2.start()

# wait for the threads to Complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)