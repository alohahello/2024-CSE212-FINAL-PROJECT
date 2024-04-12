# Queue Data Structure

## Introduction
A queue is a linear data structure that follows a particular order in which operations are performed. The order is First In First Out (FIFO). This structure is used in many real-world scenarios, including managing tasks in operating systems, handling requests on a single shared resource (like a printer), and in situations like customer service systems where the first customer in line is the first served.

## Basic Operations
- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove an element from the front of the queue.
- **Peek**: Get the element at the front of the queue without removing it.

## Python Implementation

Here's a simple implementation of a queue using Python:

```python
class Queue:
    def __init__(self):
        # Initializes a new instance of the Queue class.
        # self.queue stores all the elements in the queue.
        self.queue = []

    def enqueue(self, item):
        # Adds an item to the end of the queue.
        # The item parameter represents the item to be added.
        # Time Complexity: O(1), since appending to the end of a list is constant time.
        self.queue.append(item)

    def dequeue(self):
        # Removes and returns the item at the front of the queue.
        # If the queue is empty, it returns None.
        # Time Complexity: O(n), because popping from the beginning of a list involves shifting all other elements.
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        # Returns the item at the front of the queue without removing it.
        # If the queue is empty, returns None.
        # Time Complexity: O(1), simply retrieves the element at the first index.
        if len(self.queue) < 1:
            return None
        return self.queue[0]

    def display(self):
        # Prints all items in the queue.
        # Useful for debugging and visualizing the state of the queue.
        print(self.queue)

    def size(self):
        # Returns the number of items in the queue.
        # Time Complexity: O(1), as getting the length of a list is constant time.
        return len(self.queue)
```

## Problem: Printer Queue
**Problem Statement**: Please implement a printer queue where tasks are added to a queue and handled on a first-come, first-served basis.

**Problem File**: [Printer Queue Problem](/1.1-printer_queue_problem.py)

## Solution: Printer Queue
The solution provides a practical implementation of a printer queue system, designed to handle print tasks in a first-come, first-served order. This is achieved through a class, PrinterQueue, which encapsulates methods for enqueueing (adding) tasks, dequeueing (processing and removing) tasks, and checking the queue's size.

**Solution File**: [Printer Queue Solution](/1.2-printer_queue_solution.py)

## Exercise for You
Try implementing a queue which can handle priorities. Tasks with higher priorities should be dequeed before those with lower priorities.

## Conclusion
Queues are essential linear data structures used extensively in computing for managing data in a sequential order, adhering to the FIFO (First In, First Out) principle. Mastery of queues is invaluable in various applications, from task scheduling to buffering data streams. Understanding and implementing queues can enhance your grasp of more complex data-oriented algorithms and systems, optimizing performance and efficiency in real-world scenarios.  

[Back to Introduction Page](Introduction.md)

