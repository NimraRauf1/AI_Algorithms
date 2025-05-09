from collections import deque
class Node:
    def __init__(self, key):

        self.left = None
        self.right = None
        self.value = key

def bfs_traversal(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

def tree_height(root):
    if not root:
        return 0

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return max(left_height, right_height) + 1

root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')

print("BFS traversal:")
bfs_traversal(root)

print("\nHeight of the tree:", tree_height(root))