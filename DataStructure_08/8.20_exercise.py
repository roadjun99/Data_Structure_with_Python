from NodeSet import TNode

def level(root, node):
    if root is None:
        return 0

    if root == node:
        return 1

    queue = [(root, 1)]

    while queue:
        cur_node, cur_level = queue.pop(0)

        if cur_node:
            if cur_node == node:
                return cur_level

            queue.append((cur_node.left, cur_level + 1))
            queue.append((cur_node.right, cur_level + 1))

    return 0


c = TNode('c', None, None)
d = TNode('d', None, None)
b = TNode('b', c, d)
f = TNode('f', None, None)
e = TNode('e', None, f)
node1=TNode(c,e,d)
root = TNode('a', b, e)

print(level(root, b))
print(level(root, c))
print(level(root, e))
print(level(root,node1))