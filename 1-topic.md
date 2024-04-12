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
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


#### **5. Example Problem Solved Using Queue**
Illustrate how a queue can be used to solve a specific problem. Include both the problem statement and the solution.

```markdown
## Example Problem: Printer Queue

**Problem Statement**: Implement a printer queue where tasks are added to a queue and handled on a first-come, first-served basis.

**Solution**:

```python
printer_queue = Queue()

# Simulating tasks being added to the printer queue
printer_queue.enqueue('Print job 1')
printer_queue.enqueue('Print job 2')
printer_queue.enqueue('Print job 3')

# Process the print jobs
while printer_queue.size() > 0:
    print(f"Processing {printer_queue.dequeue()}")


#### **6. Challenges for the Reader**
Offer a problem for the reader to solve on their own to reinforce their learning. Provide a link to the solution which could be hosted on a GitHub repository or similar.

```markdown
## Exercise for You

Try implementing a queue which can handle priorities. Tasks with higher priorities should be dequeed before those with lower priorities.

[Solution](solution-link.md)

## Conclusion

In this tutorial, we explored queues, observing how they are structured and how to implement them using Python. We also saw practical examples of using queues to handle real-world problems.

[Back to Welcome Page](0-welcome.md)
