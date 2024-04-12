class Employee:
    """A class to represent an employee."""
    def __init__(self, name, emp_id):
        self.name = name  # Employee's name
        self.emp_id = emp_id  # Employee's ID
        self.next = None  # Reference to the next employee in the list

class EmployeeManagementSystem:
    """Linked list-based system to manage employee records."""
    def __init__(self):
        self.head = None  # Initially, the list is empty

    def add_employee(self, name, emp_id):
        """Add a new employee to the end of the list."""
        # Code to add a new employee
        pass

    def remove_employee(self, emp_id):
        """Remove an employee from the list using the employee ID."""
        # Code to remove an employee
        pass

    def display_employees(self):
        """Display all employee records."""
        # Code to display all employees
        pass
