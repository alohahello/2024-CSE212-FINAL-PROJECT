class PrinterQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        self.queue.append(task)
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)


# Create an instance of PrinterQueue
printer_queue = PrinterQueue()

# Simulating tasks being added to the printer queue
printer_queue.enqueue('Print job 1')
printer_queue.enqueue('Print job 2')
printer_queue.enqueue('Print job 3')

# Process the print jobs
while printer_queue.size() > 0:
    print(f"Processing {printer_queue.dequeue()}")
