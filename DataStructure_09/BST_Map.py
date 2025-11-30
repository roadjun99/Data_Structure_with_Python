from BiSearchTree import *
# 중위 순회 함수
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')  # 노드의 key만 중위 순회로 출력
        inorder(n.right)

class BSTMap:
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
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BSTMap:'):
        print(msg, end=' ')
        inorder(self.root)
        print()

if __name__ == "__main__":
    data = [33, 21, 10, 45, 38, 5, 50, 22, 40, 60, -10]
    value = ["삼삼", "이일", "일공", "사오", "삼팔", "영오", "오공", "이이", "사공", "육공", "-십"]

    map = BSTMap()
    map.display("[삽입 전]:")

    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display("[삽입 %2d]:" % data[i])

    print('[최대 키]:', map.findMax().key)
    print('[최소 키]:', map.findMin().key)
    print('[탐색 60]:', '성공' if map.search(60) is not None else '실패')
    print('[탐색 15]:', '성공' if map.search(15) is not None else '실패')
    print('[탐색 -10]:', '성공' if map.search(-10) is not None else '실패')
    print('[탐색 오공]:', '성공' if map.searchValue("오공") is not None else '실패')
    print('[탐색 이일]:', '성공' if map.searchValue("이일") is not None else '실패')

    map.delete(38)
    map.display("[삭제 38]:")
    map.delete(40)
    map.display("[삭제 40]:")
    map.delete(33)
    map.display("[삭제 33]:")
    map.delete(21)
    map.display("[삭제 21]:")
