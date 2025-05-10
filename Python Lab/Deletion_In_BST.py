class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to find the minimum value node in a tree
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Function to delete a node from the BST
def delete(root, key):
    # Base case: If the tree is empty
    if root is None:
        return root

    # Step 1: Traverse to find the node to delete
    if key < root.value:
        root.left = delete(root.left, key)
    elif key > root.value:
        root.right = delete(root.right, key)
    else:
        # Node found! Perform deletion
        # Case 1: Node with no children
        if root.left is None and root.right is None:
            return None

        # Case 2: Node with one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Node with two children
        # Find the in-order successor (smallest node in the right subtree)
        temp = find_min(root.right)
        root.value = temp.value  # Replace the node's value with successor's value
        root.right = delete(root.right, temp.value)  # Delete the successor node

    return root

# Function to perform in-order traversal to display the BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Example Usage
if __name__ == "__main__":
    root = None

    # Insert nodes into the BST
    def insert(root, key):
        if root is None:
            return Node(key)
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root

    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        root = insert(root, key)

    print("In-order traversal before deletion:")
    inorder(root)

    # Delete a node
    key_to_delete = 50
    root = delete(root, key_to_delete)

    print("\nIn-order traversal after deleting", key_to_delete, ":")
    inorder(root)
