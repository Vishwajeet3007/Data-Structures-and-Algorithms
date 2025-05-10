import threading
import time
import random

N = 5
THINKING = 2
HUNGRY = 1
EATING = 0
LEFT = lambda i: (i + N - 1) % N
RIGHT = lambda i: (i + 1) % N

state = [THINKING] * N
philosophers = list(range(N))
mutex = threading.Semaphore(1)
S = [threading.Semaphore(0) for _ in range(N)]

def test(num_of_philosopher):
    if state[num_of_philosopher] == HUNGRY and state[LEFT(num_of_philosopher)] != EATING and state[RIGHT(num_of_philosopher)] != EATING:
        state[num_of_philosopher] = EATING
        time.sleep(2)
        print(f"Philosopher {num_of_philosopher + 1} takes fork {LEFT(num_of_philosopher) + 1} and {num_of_philosopher + 1}")
        print(f"Philosopher {num_of_philosopher + 1} is Eating")
        S[num_of_philosopher].release()  # Wake up hungry philosophers

def take_fork(num_of_philosopher):
    mutex.acquire()
    state[num_of_philosopher] = HUNGRY
    print(f"Philosopher {num_of_philosopher + 1} is Hungry")
    test(num_of_philosopher)
    mutex.release()
    S[num_of_philosopher].acquire()  # Wait to be signaled
    time.sleep(1)

def put_fork(num_of_philosopher):
    mutex.acquire()
    state[num_of_philosopher] = THINKING
    print(f"Philosopher {num_of_philosopher + 1} putting fork {LEFT(num_of_philosopher) + 1} and {num_of_philosopher + 1} down")
    print(f"Philosopher {num_of_philosopher + 1} is thinking")
    test(LEFT(num_of_philosopher))
    test(RIGHT(num_of_philosopher))
    mutex.release()

def philosopher(num_of_philosopher):
    while True:
        time.sleep(1)
        take_fork(num_of_philosopher)
        put_fork(num_of_philosopher)

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()
    print(f"Philosopher {i + 1} is thinking")

for t in threads:
    t.join()
