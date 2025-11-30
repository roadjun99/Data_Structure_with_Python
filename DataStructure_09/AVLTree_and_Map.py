from CircularQueue import CircularQueue

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

# 탐색(값) - 참고용
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

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")
        return parent # 중복 시 reBalance 없이 부모 반환

def levelorder(root) :
    # 큐의 용량을 100으로 설정 (AVLTree.py와 동일하게)
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

class AVLMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, key):
        return search_bst_value(self.root, key)

    # insert_avl 사용
    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            # insert_avl은 재균형 후 새 루트를 반환하므로 self.root를 업데이트
            self.root = insert_avl(self.root, n)

    def delete(self, key):
        # 참고: 이 삭제 연산은 AVL 트리의 균형을 다시 맞추지 않습니다.
        self.root = delete_bst(self.root, key)

    # levelorder로 구조 확인
    def display(self, msg='AVLMap:'):
        print(msg, end=' ')
        levelorder(self.root)
        print()

if __name__ == "__main__":
    # 정렬된 데이터
    data = [-5,-2,0,1,3,7,9,11,24,30]
    value = ["-오", "-이", "영", "일", "삼","칠","구","십일","이십사","삼십"]

    map = AVLMap()
    map.display("[삽입 전]:")

    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display("[삽입 %2d]:" % data[i])

    print()
    print('[최대 키]:', map.findMax().key)
    print('[최소 키]:', map.findMin().key)
    print('[탐색 6]:', '성공' if map.search(3) is not None else '실패')
    print('[탐색 11]:', '성공' if map.search(11) is not None else '실패')
    print('[탐색 50]:', '성공' if map.search(50) is not None else '실패')