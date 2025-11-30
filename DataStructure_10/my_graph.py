import networkx as nx
import matplotlib.pyplot as plt

# 1. 그래프 데이터 정의 (우리가 설계한 그래프)
# 정점: 0 ~ 9
# 간선: 이전 대화에서 설계한 구조
edges = [
    (0, 1), (1, 2), (2, 0),  # 삼각형 사이클
    (2, 3), (3, 4), (4, 5),  # 직선 연결
    (5, 6), (6, 7), (7, 8), (8, 5), # 사각형 사이클
    (7, 9) # 끝부분
]
num_vertices = 10

def print_adjacency_matrix(n, edge_list):
    """인접 행렬을 생성하고 출력하는 함수"""
    # 10x10 0으로 초기화된 2차원 리스트 생성
    matrix = [[0] * n for _ in range(n)]

    for u, v in edge_list:
        matrix[u][v] = 1
        matrix[v][u] = 1 # 무방향 그래프이므로 대칭

    print(f"\n=== 인접 행렬 (Adjacency Matrix) ===")
    print("   " + " ".join([str(i) for i in range(n)])) # 헤더 출력
    for i in range(n):
        print(f"{i}: " + " ".join([str(x) for x in matrix[i]]))

    return matrix

def print_adjacency_list(n, edge_list):
    """인접 리스트를 생성하고 출력하는 함수"""
    # 빈 리스트를 포함한 딕셔너리 생성
    adj_list = {i: [] for i in range(n)}

    for u, v in edge_list:
        adj_list[u].append(v)
        adj_list[v].append(u) # 무방향 그래프

    # 보기 좋게 정렬
    for i in range(n):
        adj_list[i].sort()

    print(f"\n=== 인접 리스트 (Adjacency List) ===")
    for i in range(n):
        print(f"정점 {i}: {adj_list[i]}")

    return adj_list

def draw_graph(edge_list):
    """matplotlib과 networkx를 이용해 그래프를 그리는 함수"""
    G = nx.Graph()
    G.add_edges_from(edge_list)

    plt.figure(figsize=(8, 6)) # 그림 크기 설정

    # 그래프 레이아웃 설정 (spring_layout이 가장 보기 좋습니다)
    pos = nx.spring_layout(G, seed=42)

    # 노드, 간선, 라벨 그리기
    nx.draw(G, pos, with_labels=True,
            node_color='lightblue',
            node_size=800,
            font_size=12,
            font_weight='bold',
            edge_color='gray')

    plt.title("My Graph Visualization")
    plt.show()

# 메인 실행 코드
if __name__ == "__main__":
    # 인접 행렬 출력
    adj_matrix = print_adjacency_matrix(num_vertices, edges)

    # 인접 리스트 출력
    adj_list = print_adjacency_list(num_vertices, edges)

    # 그래프 시각화 (창이 뜸)
    print("\n그래프를 그리는 중입니다... (새 창 확인)")
    draw_graph(edges)