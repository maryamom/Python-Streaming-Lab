"""
pipeline.py
----------------
Launches both producer and consumer using threads.
"""
import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer


def main():
    import os
    csv_path = os.path.join(os.path.dirname(__file__), "transactions.csv")
    q = Queue()
    producer = CSVProducer(csv_path, q, delay=0.05)
    consumer = Consumer(q)
    t_producer = threading.Thread(target=producer.start)
    t_consumer = threading.Thread(target=consumer.start)
    t_producer.start()
    t_consumer.start()
    t_producer.join()
    t_consumer.join()


if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
