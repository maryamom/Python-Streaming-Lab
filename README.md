# Lab 1: Python Streaming Lab — Producer & Consumer Using CSV

In this lab, you will build a **simple streaming system** using only Python standard libraries.

Instead of processing data all at once, you will process events **one by one as they arrive**, simulating a real-time data stream.

---

## What Are We Building?

We are building a **producer–consumer pipeline**:

- A **Producer** reads data from a CSV file and emits events gradually
- A **Consumer** receives events and processes them immediately
- A **Queue** is used to pass events safely between components
- **Threads** allow the producer and consumer to run at the same time

---

## Project Structure

- producer.py → Reads CSV rows and streams them into a queue
- consumer.py → Reads and processes events
- pipeline.py → Runs producer + consumer simultaneously
- transactions.csv → CSV file

---

## How to Run the Lab

Run the full pipeline:

```bash
python pipeline.py
```

You should see events being produced and consumed in real time.

---

## What You Will Learn

- How streaming differs from batch processing
- The producer–consumer pattern
- How concurrency works using threads
- How events can be processed in real time
