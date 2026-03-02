"""
producer.py
----------------
Reads events from a CSV file and sends them one by one into a queue.
"""
import csv
import time
import random
from queue import Queue


class CSVProducer:
    def __init__(self, csv_path, q, delay=1.0):
        self.csv_path = csv_path
        self.q = q
        self.delay = delay

    def start(self):
        with open(self.csv_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if not row:
                    continue
                print("[Producer] Sending:", row)
                self.q.put(row)
                jitter = random.uniform(0, 0.3 * self.delay) if self.delay else 0
                time.sleep(self.delay + jitter)
        self.q.put(None)

if __name__ == "__main__":
    import os
    csv_path = os.path.join(os.path.dirname(__file__), "transactions.csv")
    q = Queue()
    producer = CSVProducer(csv_path, q, delay=0.1)
    producer.start()
