from my_weighted_graph import draw_weighted_graph
# 1. 정점 정의 (10개)
vertex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 인접 행렬 데이터
# - 정점이 10개이므로 10x10 행렬
# - 연결되지 않음: None
# - 가중치: 1 ~ 20 사이의 다양한 값

weight = [
    # 0     1     2     3     4     5     6     7     8     9
    [ 0,    5,   12, None,    8, None, None, None, None, None], # 0
    [ 5,    0,    3, None,    6,   15, None, None, None, None], # 1
    [12,    3,    0, None, None,    9,   10, None, None, None], # 2
    [None, None, None,    0,    4, None, None,   11, None, None], # 3
    [ 8,    6, None,    4,    0,    7, None,   13,    2, None], # 4
    [None, 15,    9, None,    7,    0,    1, None,   14,   20], # 5
    [None, None,   10, None, None,    1,    0, None, None,    5], # 6
    [None, None, None,   11,   13, None, None,    0,   16, None], # 7
    [None, None, None, None,    2,   14, None,   16,    0,   18], # 8
    [None, None, None, None, None,   20,    5, None,   18,    0]  # 9
]

if __name__ == "__main__":
    draw_weighted_graph(vertex, weight)
"""
[그래프 구조 설명]
- 정점 10개, 간선이 그물망처럼 연결됨
- 0번 노드에서 시작해서 9번 노드까지 가는 경로가 다양함
- 가중치가 1(5-6)부터 20(5-9)까지 다양해서 그리디 알고리즘 테스트에 적합
"""