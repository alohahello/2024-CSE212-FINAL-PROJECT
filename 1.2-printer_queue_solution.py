# --- PrinterQueue Class Definition ---
class PrinterQueue:
    def __init__(self):
        # Initialize an empty list to hold the print jobs
        self.queue = []

    def enqueue(self, task):
        # Add a new task to the end of the queue
        self.queue.append(task)
        print(f"Task '{task}' added to the printer queue.")
    
    def dequeue(self):
        # Remove and return the front task of the queue if any
        if len(self.queue) > 0:
            task = self.queue.pop(0)
            print(f"Task '{task}' is being processed.")
            return task
        else:
            print("No tasks to process.")
            return None

    def size(self):
        # Return the number of tasks in the queue
        return len(self.queue)


# --- Testing the Printer Queue ---


# Create an instance of PrinterQueue
printer_queue = PrinterQueue()

# Simulating tasks being added to the printer queue
printer_queue.enqueue('Print job 1')
printer_queue.enqueue('Print job 2')
printer_queue.enqueue('Print job 3')

# Display what's currently in the queue
print("\nStarting the printing process...\n")

# Process the print jobs
while printer_queue.size() > 0:
    # Dequeue method process and output each task
    printer_queue.dequeue()

print("\nAll print jobs have been processed.")

