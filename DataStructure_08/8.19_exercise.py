from collections import deque
from NodeSet import TNode

def is_complete_binary_tree(root):
    if root is None:
        return True

    queue = deque([root])
    flag = False

    while queue:
        node = queue.popleft()

        if node.left:
            if flag:
                return False
            queue.append(node.left)
        else:
            flag = True

        if node.right:
            if flag:
                return False
            queue.append(node.right)
        else:
            flag = True

    return True

c = TNode(12)
d = TNode(7)
b = TNode('acb', c, d)
root = TNode(b, d,c)

print(is_complete_binary_tree(root))