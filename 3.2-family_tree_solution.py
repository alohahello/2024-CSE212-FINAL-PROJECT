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
        """Add a child to a parent in the family tree.
        This function searches for the parent by name and adds a new child to them.
        """
        parent_node = self.find_member(self.root, parent_name)
        if parent_node is not None:
            parent_node.children.append(FamilyMember(child_name))
            print(f"Added {child_name} to {parent_name}'s family.")
        else:
            print(f"No parent with name {parent_name} found.")

    def find_member(self, node, name):
        """Find a member in the tree by their name using a recursive search."""
        if node.name == name:
            return node
        for child in node.children:
            found = self.find_member(child, name)
            if found:
                return found
        return None

    def display_family(self, member, level=0):
        """Display the family tree, showing each member's hierarchy."""
        print('   ' * level + member.name)
        for child in member.children:
            self.display_family(child, level + 1)

# Example Usage:
family_tree = FamilyTree("Grandparent")
family_tree.add_child("Grandparent", "Parent")
family_tree.add_child("Parent", "Child")
print("\nFamily Tree:")
family_tree.display_family(family_tree.root)
