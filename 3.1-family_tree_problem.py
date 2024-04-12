class FamilyMember:
    """A class to represent a member of a family."""
    def __init__(self, name):
        """Initialize the family member with a name and an empty list of children."""
        self.name = name
        self.children = []  # Children of this family member

class FamilyTree:
    """A class to represent the entire family tree."""
    def __init__(self, head_name):
        """Initialize the family tree with a head or root member."""
        self.root = FamilyMember(head_name)  # The root node of the family tree

    def add_child(self, parent_name, child_name):
        """Add a child to a parent in the family tree."""
        pass

    def find_member(self, node, name):
        """Recursively search for a family member by name and return the node."""
        pass

    def display_family(self, member, level=0):
        """Recursively display the family hierarchy."""
        pass

# Example Usage Without Implementation Details:
family_tree = FamilyTree("Grandparent")
family_tree.add_child("Grandparent", "Parent")
family_tree.add_child("Parent", "Child")
family_tree.display_family(family_tree.root)
