from BiSearchTree2 import *
# 중위 순회 함수
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')  # 노드의 키를 중위 순회로 출력
        inorder(n.right)

# 코드 9.11: 이진 탐색 트리를 이용한 맵 클래스
class BSTMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, value):
        return search_value_bst(self.root, value)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BSTMap :'):
        print(msg, end=' ')
        inorder(self.root)
        print()


if __name__ == "__main__":
    data = [47, 15, 7, 29, 12, 5, 68, 28, 84, 99]
    value = ["사칠", "일오", "영칠", "이구", "일이", "영오", "육팔", "이팔", "팔사", "구구"]

    map = BSTMap()
    map.display("[삽입 전] : ")

    for i in range(len(data)):
        map.insert(data[i], value[i])
        map.display("[삽입 %2d] : " % data[i])

    print('[최대 키] :', map.findMax().key)
    print('[최소 키] :', map.findMin().key)
    print('[탐색 29] :', '성공' if map.search(29) is not None else '실패')
    print('[탐색 25] :', '성공' if map.search(25) is not None else '실패')
    print('[탐색 이팔] :', '성공' if map.searchValue("이팔") is not None else '실패')
    print('[탐색 이칠] :', '성공' if map.searchValue("이칠") is not None else '실패')

    map.delete(5)
    map.display("[삭제  5] : ")
    map.delete(28)
    map.display("[삭제 28] : ")
    map.delete(47)
    map.display("[삭제 47] : ")
    map.delete(15)
    map.display("[삭제 15] : ")
