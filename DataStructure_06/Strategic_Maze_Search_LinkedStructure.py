from Linked_Stack import *
from Circular_Linked_Queue import LinkedQueue
from Doubly_Linked_Deque import *

import math
import os
import time
import copy
map = [
    ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■'],
    ['→', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', '■'],
    ['■', '■', '■', ' ', '■', ' ', '■', '■', '■', ' ', '■', ' ', '■', ' ', '■', ' ', '■', '■', ' ', '■'],
    ['■', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', '■', ' ', ' ', '■'],
    ['■', ' ', '■', '■', '■', '■', '■', ' ', '■', '■', '■', '■', '■', '■', '■', ' ', '■', ' ', '■', '■'],
    ['■', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', '■'],
    ['■', '■', '■', '■', '■', ' ', '■', '■', '■', ' ', '■', '■', '■', '■', '■', ' ', '■', '■', ' ', '■'],
    ['■', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', ' ', '■'],
    ['■', ' ', '■', ' ', '■', '■', '■', ' ', '■', '■', '■', '■', '■', ' ', '■', '■', '■', '■', ' ', '■'],
    ['■', ' ', '■', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', '■'],
    ['■', ' ', '■', '■', '■', '■', '■', ' ', '■', ' ', '■', '■', '■', ' ', '■', ' ', '■', '■', '■', '■'],
    ['■', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', '■', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', '■'],
    ['■', '■', '■', ' ', '■', ' ', '■', '■', '■', '■', '■', ' ', '■', '■', '■', '■', '■', ' ', '■', '■'],
    ['■', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '■', '■'],
    ['■', ' ', '■', '■', '■', '■', '■', '■', '■', '■', '■', ' ', '■', '■', '■', ' ', '■', ' ', ' ', '■'],
    ['■', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '■', '■', ' ', '■'],
    ['■', '■', '■', '■', '■', ' ', '■', '■', '■', ' ', '■', '■', '■', ' ', '■', ' ', ' ', ' ', ' ', '■'],
    ['■', ' ', ' ', ' ', ' ', ' ', '■', ' ', ' ', ' ', '■', ' ', ' ', ' ', '■', '■', '■', '■', ' ', '■'],
    ['■', ' ', '■', '■', '■', '■', '■', ' ', '■', ' ', ' ', ' ', '■', ' ', ' ', ' ', ' ', ' ', ' ', '★'],
    ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
]
MAX_MAZE=20
(ox,oy)=(18,19)

def dist(x,y):
    (dx,dy)=(ox-x,oy-y)
    return math.sqrt(dx*dx+dy*dy)

def print_maze(maze):
    for row in maze:
        for char in row:
            if char == ' ':
                print('  ', end='') # 공백은 두 칸으로 출력
            else:
                print(f'{char} ', end='')
        print() # 다음 줄로 이동

def isValidPos(x,y):
    if 0<=x<MAX_MAZE and 0<=y<MAX_MAZE:
        if map[y][x]==' ' or map[y][x]=='★':
            return True
    return False

def DFS():
    stack=DoublyLinkedDeque()
    stack.addRear((0,1))

    while not stack.isEmpty():
        os.system('cls')
        here=stack.deleteRear()
        (x,y)=here
        print_maze(map)
        print("현재 위치 :",here)
        print()
        time.sleep(0.5)
        if(map[y][x]=='★'):
            os.system('cls')
            print_maze(map)
            print("현재 위치 :", here)
            print("미로 탐색 성공!")
            return True
        else:
            map[y][x]='√'
            if isValidPos(x,y-1): stack.addRear((x,y-1))   #상
            if isValidPos(x, y+1): stack.addRear((x, y+1)) #하
            if isValidPos(x-1, y): stack.addRear((x-1, y)) #좌
            if isValidPos(x+1, y): stack.addRear((x+1, y)) #우

    return False

def BFS():
    que=LinkedQueue()
    que.enqueue((0,1))

    while not que.isEmpty():
        os.system('cls')
        here=que.dequeue()
        (x,y)=here
        print_maze(map)
        print("현재 위치 :", here)
        print()
        time.sleep(0.5)
        if (map[y][x] == '★'):
            os.system('cls')
            print_maze(map)
            print("현재 위치 :", here)
            print("미로 탐색 성공!")
            return True
        else:
            map[y][x]='√'
            if isValidPos(x,y-1):que.enqueue((x,y-1))
            if isValidPos(x, y+1): que.enqueue((x, y+1))
            if isValidPos(x-1, y): que.enqueue((x-1, y))
            if isValidPos(x+1, y): que.enqueue((x+1, y))
    return False

os.system('cls')
while True :
        print_maze(map)
        select =input("탐색 방법 : \n1 = DFS\n2 = BFS\nq = 종료\n")

        map =copy.deepcopy(map)
        if select =='1' :
            if not DFS() :
                print("미로 탐색 실패")

        elif select =='2' :
            if not BFS() :
                print("미로 탐색 실패")

        elif select =='q' :
            break

        else :
            print("입력 오류")