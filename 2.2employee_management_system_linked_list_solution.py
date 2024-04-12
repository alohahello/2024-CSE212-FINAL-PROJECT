class Employee:
    """A class to represent an employee."""
    def __init__(self, name, emp_id):
        """Initialize a new Employee node with name, ID, and reference to next node."""
        self.name = name  # Employee's name
        self.emp_id = emp_id  # Employee's ID
        self.next = None  # Reference to the next employee in the list

class EmployeeManagementSystem:
    """Linked list-based system to manage employee records."""
    def __init__(self):
        """Initialize the Employee Management System with an empty list (no head)."""
        self.head = None  # Initially, the list is empty

    def add_employee(self, name, emp_id):
        """Add a new employee to the end of the list."""
        new_employee = Employee(name, emp_id)  # Create a new employee instance
        if self.head is None:
            self.head = new_employee  # If list is empty, set new employee as the head
        else:
            last = self.head
            while last.next:  # Traverse to the last employee in the list
                last = last.next
            last.next = new_employee  # Set last employee's next to new employee
        print(f"Employee {name} added.")

    def remove_employee(self, emp_id):
        """Remove an employee from the list using the employee ID."""
        current = self.head  
        previous = None
        while current and current.emp_id != emp_id:
            previous = current  # Keep track of the previous employee
            current = current.next  # Move to the next employee
        
        if current is None:
            print("Employee not found.")
            return False

        if previous is None:
            self.head = current.next  # Remove the head employee if it's the match
        else:
            previous.next = current.next  # Bypass the removed employee
        print(f"Employee ID {emp_id} removed.")
        return True

    def display_employees(self):
        """Display all employee records in the system."""
        current = self.head
        if current is None:
            print("No employees in the system.")
            return
        
        print("Employee List:")
        while current:
            print(f"Name: {current.name}, ID: {current.emp_id}")  # Display each employee
            current = current.next

# Example Usage
ems = EmployeeManagementSystem()
ems.add_employee("John Doe", "E123")
ems.add_employee("Jane Smith", "E124")
ems.display_employees()
ems.remove_employee("E123")
ems.display_employees()
