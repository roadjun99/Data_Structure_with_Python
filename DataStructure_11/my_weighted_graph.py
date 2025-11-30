import networkx as nx
import matplotlib.pyplot as plt

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# 인접 행렬
# 연결되지 않은 곳은 None으로 표시 (교재의 MST 코드 호환용)
# 대각선(자신에게 가는 경로)은 0

weight = [
    # A     B     C     D     E     F     G
    [ 0,    8,    3, None, None, None, None], # A
    [ 8,    0, None,    9,    4, None, None], # B
    [ 3, None,    0,    5, None,    7, None], # C
    [None,  9,    5,    0,    2,    6,   10], # D
    [None,  4, None,    2,    0, None,    5], # E
    [None, None,    7,    6, None,    0,    8], # F
    [None, None, None,   10,    5,    8,    0]  # G
]

def draw_weighted_graph(vtx, adj):
    G = nx.Graph()

    # 정점 추가
    G.add_nodes_from(vtx)

    # 간선 및 가중치 추가
    n = len(vtx)
    for i in range(n):
        for j in range(i + 1, n):  # 무방향이므로 한쪽만 확인
            if adj[i][j] is not None and adj[i][j] != 0:
                G.add_edge(vtx[i], vtx[j], weight=adj[i][j])

    pos = nx.spring_layout(G, seed=7)  # 레이아웃 고정

    plt.figure(figsize=(8, 6))

    # 노드 그리기
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # 간선 그리기
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')

    # 가중치 라벨 그리기
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title("My Weighted Graph")
    plt.show()


if __name__ == "__main__":
    draw_weighted_graph(vertex, weight)