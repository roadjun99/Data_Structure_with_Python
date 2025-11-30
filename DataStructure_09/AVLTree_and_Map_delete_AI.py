# --- CircularQueue.py 의 내용 ---
# AI에 CircularQueue 파일을 학습시켰더니 이런 식으로 코딩을 해주었습니다.
class CircularQueue:
    def __init__(self, capacity=8):
        self.capacity = capacity  # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0  # 전단의 인덱스
        self.rear = 0  # 후단의 인덱스

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.front < self.rear:
            return str(self.array[self.front + 1:self.rear + 1])
        else:
            return str(self.array[self.front + 1:self.capacity] + \
                       self.array[0:self.rear + 1])


# --- BiSearchTree.py / BiSearchTree2.py 에서 가져온 노드 클래스 및 기본 함수 ---

# 노드 클래스
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None


# 탐색(키 값)
def search_bst(n, key):
    if n == None:
        return None
    elif n.key == key:
        return n
    elif n.key < key:
        return search_bst(n.right, key)
    else:
        return search_bst(n.left, key)


# 탐색(값) - 참고용
def search_bst_value(n, value):
    if n == None:
        return None
    elif n.value == value:
        return n

    res = search_bst_value(n.left, value)
    if res is not None:
        return res
    else:
        return search_bst_value(n.right, value)


# 최대 최소 키 값
def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n


def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n


# --- AVLTree.py 에서 가져온 AVL 관련 함수들 ---
#

def calc_height(n):
    if n is None: return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1


# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)


# 코드 9.14: AVL 트리의 LL회전
def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B


# 코드 9.15: AVL 트리의 RR회전
def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B


# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)


# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)


# 코드 9.18: AVL 트리의 재균형 함수
# (삭제 연산에서는 이 함수 대신 reBalance_delete를 사용합니다)
def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent


# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)  # 삽입 시 재균형

    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent);  # 삽입 시 재균형
    else:
        print("중복된 키 에러")
        return parent


# ⭐️ --- [새로 추가] AVL 트리의 삭제 연산 --- ⭐️

# 삭제를 위한 재균형 함수
# (삽입 시 reBalance와 달리, 자식의 균형 인수를 확인하는 방식이 다름)
def reBalance_delete(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:  # 왼쪽 서브트리가 더 높음
        # 자식(parent.left)의 균형 인수가 0 이상이면 LL (또는 균형)
        if calc_height_diff(parent.left) >= 0:
            parent = rotateLL(parent)
        # 자식의 균형 인수가 0 미만이면 LR
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:  # 오른쪽 서브트리가 더 높음
        # 자식(parent.right)의 균형 인수가 0 이하이면 RR (또는 균형)
        if calc_height_diff(parent.right) <= 0:
            parent = rotateRR(parent)
        # 자식의 균형 인수가 0 초과이면 RL
        else:
            parent = rotateRL(parent)
    return parent


def delete_avl(root, key):
    if root is None:
        return None  # 삭제할 노드가 없음

    # 1. 일반 BST 삭제 연산 수행
    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
    else:  # 삭제할 노드(root)를 찾음
        # Case 1 & 2: 자식이 0개 또는 1개
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Case 3: 자식이 2개
        succ = search_min_bst(root.right)  # 오른쪽 서브트리의 최소값(후계자)
        root.key = succ.key
        root.value = succ.value
        # 후계자를 삭제 (재귀 호출)
        root.right = delete_avl(root.right, succ.key)

    # 2. 삭제 후 재균형 수행 (핵심!)
    # (root가 None이 된 경우 - 예: 리프 노드 삭제 - 를 처리)
    if root is None:
        return None

    return reBalance_delete(root)


# 레벨 순회 (CircularQueue 사용)
def levelorder(root):
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


# --- AVLMap 클래스 (delete 수정) ---

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

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

            # ⭐️ [핵심 수정] delete_bst 대신 delete_avl 사용

    def delete(self, key):
        if not self.isEmpty():
            self.root = delete_avl(self.root, key)

    def display(self, msg='AVLMap:'):
        print(msg, end=' ')
        levelorder(self.root)
        print()


# --- [새로 추가] 삭제 연산 테스트 프로그램 ---
if __name__ == "__main__":
    # 1. 정렬된 데이터 삽입 (삽입 테스트)
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]

    map = AVLMap()
    print("--- [삽입 테스트] (정렬된 데이터) ---")
    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display("[삽입 %2d]:" % data[i])

    print("\n--- [삽입 완료 후 최종 트리] ---")
    map.display("          :")  # 최종: 3 1 7 0 2 5 8 4 6 9

    print("\n--- [삭제 테스트] ---")

    # Case 1: 리프 노드 삭제 (9) -> 간단 삭제
    map.delete(9)
    map.display("[삭제  9]:")  # 3 1 7 0 2 5 8 4 6

    # Case 2: 삭제 후 회전 발생 (8 삭제)
    # (6의 오른쪽 자식이던 8이 사라지며 7, 5, 4, 6 경로가 불균형)
    map.delete(8)
    map.display("[삭제  8]:")  # 3 1 5 0 2 4 7 6
    # (7이 6의 부모가 됨 - RL 회전 발생)

    # Case 3: 삭제 후 회전 발생 (4 삭제)
    map.delete(4)
    map.display("[삭제  4]:")  # 3 1 6 0 2 5 7
    # (5가 6의 부모가 됨 - RR 회전 발생)

    # Case 4: 루트 노드 삭제 (3)
    map.delete(3)
    map.display("[삭제  3]:")  # 5 1 6 0 2 7
    # (후계자인 5가 새 루트가 됨)