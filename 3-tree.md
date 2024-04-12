# Tree Data Structure

## Introduction
A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges. It represents hierarchical data like file systems or organizational structures. Unlike other data structures, trees reflect a parent-child relationship among nodes.

## Key Terminologies
- **Root**: The top node in a tree.
- **Child**: A node directly connected to another node when moving away from the Root.
- **Parent**: The converse notion of a child.
- **Siblings**: Nodes sharing the same parent.
- **Leaf**: A node that does not have any child node.
- **Depth**: The length of the path from the root to the node.
- **Height**: The length of the path from the node to the deepest leaf.


## Types of Trees
- **Binary Tree**: Each node has at most two children referred to as `left child` and `right child`.
- **Binary Search Tree (BST)**: A binary tree where each node has a comparable key (and an associated value) and satisfies the restriction that the key in any node is larger than the keys in all nodes in its left sub-tree and smaller than the keys in all nodes in its right sub-tree.
- **AVL Tree**: A self-balancing binary search tree where the difference between heights of left and right subtrees cannot be more than one for all nodes.

## Practical Application
A tree can be utilized to organize a file system, where folders may contain files or other folders, showcasing the efficient structure and retrieval capabilities of trees.

## Implementation of Binary Search Tree
```python
class Node:
    """A node in the Binary Search Tree."""
    def __init__(self, key):
        """Initialize the node with a key, and left and right pointers set to None."""
        self.left = None  # Pointer to left child
        self.right = None  # Pointer to right child
        self.val = key  # Node's value

class BST:
    """Binary Search Tree implementation."""
    def __init__(self):
        """Initialize the root of the BST to None."""
        self.root = None  # Root node of the BST

    def insert(self, key):
        """Insert a node into the BST.
        Time Complexity: O(log n) on average; O(n) in the worst case when the tree becomes skewed.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, cur_node, key):
        """Recursive helper method to insert a node into the BST.
        Time Complexity: O(log n) on average; O(n) in the worst case when the tree becomes skewed.
        """
        if key < cur_node.val:
            if cur_node.left is None:
                cur_node.left = Node(key)
            else:
                self._insert(cur_node.left, key)
        else:
            if cur_node.right is None:
                cur_node.right = Node(key)
            else:
                self._insert(cur_node.right, key)

    def inorder_traversal(self, root):
        """Perform an in-order traversal of the BST.
        Time Complexity: O(n), where n is the number of nodes in the tree.
        """
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.val)
            res += self.inorder_traversal(root.right)
        return res
```

## Problem: Family Tree
**Problem Statement**: Implement a Family Tree using a tree data structure in which each node represents a family member. The tree should allow adding family members and displaying the family hierarchy.

**Hint**: In a family tree, each person (node) will typically have links to their children, making it a clear example of a hierarchical system. Operations might include adding a new child to a specific parent and displaying the family structure.

**Problem File**: [Family Tree Problem](/3.1-family_tree_problem.py)

## Solution: Family Tree
The solution provides a practical implementation of a Family Tree Management System, designed to manage family members and their relationships efficiently using a tree data structure. This is achieved through a class, FamilyTree, which encapsulates methods for adding family members, searching for specific members, and displaying the family hierarchy dynamically.

**Solution File**: [Family Tree Solution](/3.2-family_tree_solution.py)

## Exercise for You
Try implementing a Balanced Binary Search Tree (BST) where operations such as insertions, deletions, and lookups automatically maintain the tree's balanced state. Enhance the system so you can perform these operations more efficiently to ensure an optimal time complexity in all scenarios.

## Conclusion
The tree data structure is versatile, enabling efficient data management and retrieval, suitable for applications where data is naturally hierarchical. By mastering tree structures, you can enhance your understanding of complex algorithms and improve system organization.

[Back to Introduction Page](/Introduction.md)