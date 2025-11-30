from collections import deque
from NodeSet import TNode

def path_length(root):
    if root is None:
        return 0

    total_path_length = 0
    queue = deque([(root, 0)])

    while queue:
        node, depth = queue.popleft()
        total_path_length += depth

        if node.left:
            queue.append((node.left, depth + 1))

        if node.right:
            queue.append((node.right, depth + 1))

    return total_path_length


c = TNode('c')
b = TNode('b', c, None)
root = TNode('a', b, None)


print("경로의 길이:", path_length(root))