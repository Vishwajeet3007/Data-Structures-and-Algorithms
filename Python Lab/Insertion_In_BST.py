class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a new node into the BST
def insert(root, key):
    # If the tree is empty, create a new node
    if root is None:
        return Node(key)
    
    # Traverse the tree to find the correct position
    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)
    
    # Return the unchanged root node
    return root

# Function to perform an in-order traversal to display the BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Example Usage
if __name__ == "__main__":
    root = None
    keys = [50, 30, 70, 20, 40, 60, 80]  # Sample input keys

    # Insert keys into the BST
    for key in keys:
        root = insert(root, key)
    
    print("In-order traversal of the BST:")
    inorder(root)
