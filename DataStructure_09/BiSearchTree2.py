# 코드 9.1: 이진 탐색 트리를 위한 노드 클래스
class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

# 코드 9.2: 이진 탐색 트리의 탐색 연산 (순환 구조)
def search_bst(n, key):
    if n is None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

# 코드 9.3: 이진 탐색 트리의 탐색 연산 (반복 구조)
def search_bst_iter(n, key):
    while n is not None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

# 코드 9.4: 이진 탐색 트리의 값을 이용한 탐색 연산
def search_value_bst(n, value):
    if n is None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    return search_value_bst(n.right, value)

# 코드 9.5: 최대와 최소 키를 가지는 노드 탐색 연산
def search_max_bst(n):
    if n is None or n.right is None:
        return n
    return search_max_bst(n.right)

def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

# 코드 9.6: 이진 탐색 트리의 삽입 연산 (반복 구조)
def insert_bst(r, n):
    while r:
        if n.key < r.key:
            if r.left is None:
                r.left = n
                return True
            else:
                r = r.left
        elif n.key > r.key:
            if r.right is None:
                r.right = n
                return True
            else:
                r = r.right
        else:
            return False

# 코드 9.7: 단말 노드의 삭제 연산 (case 1)
def delete_bst_case1(parent, node, root):
    if parent is None:  # 삭제할 단말 노드가 루트인 경우
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root

# 코드 9.8: 자식이 하나인 노드의 삭제 연산 (case 2)
def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root

# 코드 9.9: 자식이 둘인 노드의 삭제 연산 (case 3)
def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right

    while succ.left is not None:
        succp = succ
        succ = succ.left

    if succp.left == succ:
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    return root

# 코드 9.10: 이진 탐색 트리의 삭제 연산
def delete_bst(root, key):
    if root is None:
        return None

    parent = None
    node = root

    # 삭제할 노드 탐색
    while node is not None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node is None:
        return root  # 삭제할 노드가 없음

    # case 1: 단말 노드
    if node.left is None and node.right is None:
        root = delete_bst_case1(parent, node, root)
    # case 2: 하나의 자식을 가진 노드
    elif node.left is None or node.right is None:
        root = delete_bst_case2(parent, node, root)
    # case 3: 두 개의 자식을 가진 노드
    else:
        root = delete_bst_case3(parent, node, root)

    return root