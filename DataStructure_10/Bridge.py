from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from my_graph import edges, num_vertices


def get_adjacency_list(n, edge_list):
    """간선 리스트를 이용해 인접 리스트를 생성하는 헬퍼 함수"""
    adj = [[] for _ in range(n)]
    for u, v in edge_list:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def is_connected_bfs(n, adj_list):
    """
    인접 리스트 기반의 BFS로 그래프 연결성 확인
    반환값: True(모든 정점 연결됨), False(끊어짐)
    """
    visited = [False] * n

    # 0번 정점에서 탐색 시작
    queue = deque([0])
    visited[0] = True
    count = 1

    while queue:
        u = queue.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                count += 1
                queue.append(v)

    # 방문한 정점 수가 전체 정점 수와 같으면 연결된 상태
    return count == n


def find_all_bridges(n, edge_list):
    """
    리스트에서 간선을 직접 제거/복구하며 브리지를 찾는 함수
    """
    bridges = []
    # 1. 초기 인접 리스트 생성
    adj_list = get_adjacency_list(n, edge_list)

    print("\n--- 브리지 탐색 시작 (인접 리스트 방식) ---")

    for u, v in edge_list:
        # 2. 간선 제거 (리스트에서 잠시 삭제)
        # u의 리스트에서 v를, v의 리스트에서 u를 삭제
        adj_list[u].remove(v)
        adj_list[v].remove(u)

        # 3. 연결 여부 확인 (BFS)
        if not is_connected_bfs(n, adj_list):
            print(f"발견! 간선 ({u}, {v}) 제거 시 연결 끊김 -> 브리지 O")
            bridges.append((u, v))

        # 4. 간선 복구 (다시 추가)
        adj_list[u].append(v)
        adj_list[v].append(u)

    return bridges


def draw_bridges(original_edges, bridge_edges):
    """시각화 함수 (이전과 동일)"""
    G = nx.Graph()
    G.add_edges_from(original_edges)

    plt.figure(figsize=(10, 7))
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=800)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # 일반 간선 (전체 - 브리지)
    bridge_set = set([tuple(sorted(e)) for e in bridge_edges])
    normal_edges = [e for e in original_edges if tuple(sorted(e)) not in bridge_set]

    nx.draw_networkx_edges(G, pos, edgelist=normal_edges, edge_color='gray', width=2)

    # 브리지 (빨간색 굵은 실선)
    nx.draw_networkx_edges(G, pos, edgelist=bridge_edges, edge_color='red', width=4)

    plt.title("Bridge Detection (Adjacency List Implementation)")
    plt.show()


if __name__ == "__main__":
    # 1. 브리지 찾기
    found_bridges = find_all_bridges(num_vertices, edges)

    print("\n=== 탐색 결과 ===")
    print(f"찾아낸 브리지 목록: {found_bridges}")

    # 2. 시각화
    print("그래프 창을 띄우는 중입니다...")
    draw_bridges(edges, found_bridges)