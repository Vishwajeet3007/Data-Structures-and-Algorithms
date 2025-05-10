import threading
import time

mutex = 1
full = 0
empty = 10
x = 0

def producer():
    global mutex, full, empty, x
    while True:
        if mutex == 1 and empty != 0:
            mutex -= 1
            full += 1
            empty -= 1
            x += 1
            print(f"\nProducer produces item {x}")
            mutex += 1
        else:
            print("Buffer is full!")
        time.sleep(0.5)

def consumer():
    global mutex, full, empty, x
    while True:
        if mutex == 1 and full != 0:
            mutex -= 1
            full -= 1
            empty += 1
            print(f"\nConsumer consumes item {x}")
            x -= 1
            mutex += 1
        else:
            print("Buffer is empty!")
        time.sleep(0.5)

if __name__ == "__main__":
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
