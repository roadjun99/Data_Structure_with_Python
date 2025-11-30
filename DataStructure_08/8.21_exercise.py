from NodeSet import TNode

def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1

def is_balanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(root.left) and is_balanced(root.right)

c = TNode('c', None, None)
d = TNode('d', None, None)
b = TNode('b', c, d)
f = TNode('f', None, None)
e = TNode('e', None, f)
root = TNode('a', b, e)


print("균형 잡혀있는지 판별")
print(is_balanced(root))