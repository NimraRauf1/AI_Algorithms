class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_recursive(node):
    if node is None:
        return
    print(node.value, end=" ")
    dfs_recursive(node.left)
    dfs_recursive(node.right)


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')

print("DFS Traversal (Pre-order):")
dfs_recursive(root)