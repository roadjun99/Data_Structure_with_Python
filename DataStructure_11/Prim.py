from my_weighted_graph import vertex, weight

INF = 9999

def getMinVertex(dist, selected):
    minv = -1
    mindist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

# MSTPrim 함수 수정
def MSTPrim(vertex, adj):
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0  # 시작 정점의 거리=0

    mst_weight_sum = 0  # 가중치 합

    print("\nPrim 알고리즘: 최소 비용 신장 트리 구하기")

    for i in range(vsize):
        # 트리에 연결되지 않은 정점 중 가장 가까운 정점(u) 선택
        u = getMinVertex(dist, selected)
        selected[u] = True

        # 선택된 정점까지의 거리를 총합에 누적
        mst_weight_sum += dist[u]

        print(f"정점 선택: {vertex[u]} (연결 비용: {dist[u]})")

        # 선택된 정점 u를 기준으로 인접한 정점들의 거리(dist) 갱신
        for v in range(vsize):
            if (adj[u][v] is not None):  # 간선 있으면
                if not selected[v] and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]

    # 최종 가중치 합
    print(f"\nMST의 가중치 합 (Total Weight): {mst_weight_sum}")


if __name__ == "__main__":
    MSTPrim(vertex, weight)