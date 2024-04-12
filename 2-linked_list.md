# Linked List Data Structure

## Introduction
A linked list is a linear data structure that includes a series of connected nodes. Each node stores the data and a pointer to the next node in the sequence. This structure allows for efficient insertion and deletion of elements at any position, unlike arrays which require shifting elements.

## Types of Linked Lists
- **Singly Linked List**: Each node has a single link field pointing to the next node.
- **Doubly Linked List**: Nodes have two links, one pointing to the next node and another to the previous one.
- **Circular Linked List**: Similar to singly or doubly but the last node points back to the first node, making the list circular.


## Python Implementation
Here's a simple implementation of a basic singly linked list using Python:

```python
class Node:
    """A class to represent a node in a linked list."""
    def __init__(self, data):
        """Initialize a new node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class LinkedList:
    """A class to represent a singly linked list."""
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None  # Head points to the first element of the list.

    def insert(self, data):
        """Insert a node with the specified data at the beginning of the list.
        Time Complexity: O(1), as insertion at the head involves constant time operations.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Deletes the first node containing the specified data from the list.
        Time Complexity: O(n), where n is the number of nodes in the list (in the worst case).
        """
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        
        if current is None:
            return  # The data was not found.

        if previous is None:
            self.head = current.next  # The node to delete is the head.
        else:
            previous.next = current.next

    def search(self, key):
        """Searches for a node with a specified value.
        Time Complexity: O(n), where n is the number of nodes (in the worst case).
        Returns True if found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def reverse(self):
        """Reverses the linked list.
        Time Complexity: O(n), where n is the number of nodes.
        """
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        """Prints all elements in the list.
        Time Complexity: O(n), where n is the number of nodes.
        """
        current = self.head
        while current:
            print(current.data, end=' -> ')
        print('None')

```

## Problem: Employee Management System
**Problem Statement**: Please implement an Employee Management System using a linked list where employee records can be added and removed efficiently.

**Problem File**: [Employee Management System Problem](/2.1employee_management_system_linked_list_problem.py)

## Solution: Employee Management System
The solution provides a practical implementation of an Employee Management System, designed to manage employee records efficiently using a linked list. This is achieved through a class, EmployeeManagementSystem, which encapsulates methods for adding, removing, and managing employee records dynamically.

**Solution File**: [Employee Management System Solution](/2.2employee_management_system_linked_list_solution.py)

## Exercise for You
Try implementing a doubly linked list where each node keeps a reference to both the next and the previous node. Enhance the system so you can delete nodes from the middle of the list more efficiently.

## Conclusion
Linked lists are dynamic data structures that are fundamental in computer science for managing collections of elements. Mastery of linked lists can help improve your understanding of more complex data structures.


[Back to Introduction Page](/Introduction.md)
