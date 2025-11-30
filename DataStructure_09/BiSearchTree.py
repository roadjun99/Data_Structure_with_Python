# 노드 클래스
class BSTNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None

    def isLeaf(self):
        return self.left is None and self.right is None

# 탐색(키 값)
def search_bst(n,key):
    if n==None:
        return None

    elif n.key==key:
        return n

    elif n.key<key:
        return search_bst(n.right,key)

    else:
        return search_bst(n.left,key)

# 탐색(키 값, 반복구조)
def search_bst_iter(n, key):
    while n is not None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

# 탐색(값)
def search_bst_value(n,value):
    if n==None:
        return None
    elif n.value==value:
        return n

    res=search_bst_value(n.left,value)
    if res is not None:
        return res
    else:
        return search_bst_value(n.right,value)

# 최대 최소 키 값
def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n

def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

# 이진 탐색 트리의 삽입 연산 (순환 구조)
def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False

# 이진 탐색 트리 삭제
def delete_bst(root,key):
    if root==None:
        return root

    if key<root.key:
        root.left= delete_bst(root.left,key)
    elif key>root.key:
        root.right=delete_bst(root.right,key)

    else:
        if root.left==None:
            return root.right
        if root.right==None:
            return root.left

        succ=search_min_bst(root.right) # 오른쪽 서브트리 최솟값
        root.key=succ.key
        root.value=succ.value
        root.right=delete_bst(root.right,succ.key)

    return root