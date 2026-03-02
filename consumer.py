"""
consumer.py
----------------
Continuously reads messages from the queue and processes them.
"""
import time
from queue import Queue


class Consumer:
    def __init__(self, q):
        self.q = q
        self.running_total = 0.0
        self.count = 0

    def start(self):
        while True:
            event = self.q.get()
            if event is None:
                break
            print("[Consumer] Received:", event)
            self.process(event)
        print("[Consumer] Done. Total amount:", self.running_total, "Count:", self.count)

    def process(self, event):
        time.sleep(0.05)
        if len(event) >= 3:
            try:
                amount = float(event[2])
                self.running_total += amount
                self.count += 1
            except (ValueError, IndexError):
                pass

if __name__ == "__main__":
    q = Queue()
    consumer = Consumer(q)
    consumer.start()
