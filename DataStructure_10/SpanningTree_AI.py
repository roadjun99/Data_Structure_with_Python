from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt
from my_graph import edges, num_vertices, print_adjacency_matrix


# [수정된 구현] BFS 신장 트리 + 시각화 데이터 수집
def ST_BFS_Visual(vtx, adj, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    st_edges = []  # 시각화를 위해 간선을 저장할 리스트

    while not Q.empty():
        s = Q.get()

        for v in range(n):
            if adj[s][v] != 0:
                if visited[v] == False:
                    # 1. 텍스트 출력 (교재 스타일)
                    print("(", vtx[s], vtx[v], ")", end=' ')

                    # 2. 시각화용 데이터 저장
                    st_edges.append((s, v))

                    Q.put(v)
                    visited[v] = True

    return st_edges


def draw_spanning_tree(original_edges, tree_edges):
    """원래 그래프 위에 신장 트리를 덧그려 시각화하는 함수"""
    G = nx.Graph()
    G.add_edges_from(original_edges)

    plt.figure(figsize=(10, 7))
    # 그래프 모양 고정 (seed=42)
    pos = nx.spring_layout(G, seed=42)

    # 1. 전체 그래프 (회색 점선으로 배경)
    nx.draw_networkx_nodes(G, pos, node_color='lightgray', node_size=800)
    nx.draw_networkx_edges(G, pos, edge_color='lightgray', style='dashed')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # 2. 신장 트리 (빨간색 실선으로 강조)
    # tree_edges의 정점 번호가 (0, 1) 형태이므로 그대로 그립니다.
    nx.draw_networkx_edges(G, pos, edgelist=tree_edges, edge_color='red', width=3)

    plt.title("BFS Spanning Tree Visualization (Red Lines)")
    plt.show()


if __name__ == "__main__":
    print("\n--- 4. 신장 트리 (BFS & 시각화 포함) ---")

    # 1. 데이터 준비
    vtx = [i for i in range(num_vertices)]
    adj_matrix = print_adjacency_matrix(num_vertices, edges)

    print('\n신장트리(BFS) 간선 출력: ', end="")

    # 2. BFS 수행 및 간선 리스트 획득
    spanning_tree_edges = ST_BFS_Visual(vtx, adj_matrix, 0)
    print()  # 줄바꿈

    # 3. 그래프 그리기
    print("\n그래프 창을 띄우는 중입니다...")
    draw_spanning_tree(edges, spanning_tree_edges)