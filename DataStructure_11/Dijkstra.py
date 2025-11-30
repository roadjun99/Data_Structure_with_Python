from my_weighted_graph import vertex, weight

INF = 9999  # 무한대 값 설정


# 방문하지 않은 노드 중 최소 거리 노드 선택
def choose_vertex(dist, found):
    min_val = INF
    minpos = -1

    for i in range(len(dist)):
        # 아직 방문하지 않았고(found[i] == False) 가장 거리가 짧은 정점 선택
        if dist[i] < min_val and not found[i]:
            min_val = dist[i]
            minpos = i
    return minpos

# 다익스트라 알고리즘
def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)

    # dist 배열 초기화 (시작 정점의 행을 복사)
    dist = list(adj[start])

    # 경로 저장(초기값은 시작 정점)
    path = [start] * vsize

    # 방문 여부 배열
    found = [False] * vsize

    # 시작 정점 초기화
    found[start] = True
    dist[start] = 0

    for i in range(vsize):
        # 단계별 dist 배열 상태 출력
        print("Step%2d: " % (i + 1), dist)

        # 최소 거리 정점 선택
        u = choose_vertex(dist, found)

        # 더 이상 갈 곳이 없거나 모든 연결된 곳을 방문했으면 중단
        if u == -1:
            break

        found[u] = True

        # 거리 갱신
        for w in range(vsize):
            if not found[w]:  # 아직 방문하지 않은 정점에 대해
                # 간선이 존재하고(INF가 아님) 거쳐가는 것이 더 빠르다면 갱신
                if adj[u][w] != INF and (dist[u] + adj[u][w] < dist[w]):
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u  # 경로 기록 (이전 정점이 u임을 저장)

    return path, dist


if __name__ == "__main__":
    # 우리가 만든 그래프는 연결 안 됨을 None으로 표시하므로 다익스트라 계산을 위해 이를 INF로 바꿔준 새로운 행렬 만들기
    adj_mat = []
    for row in weight:
        new_row = []
        for val in row:
            if val is None:
                new_row.append(INF)
            else:
                new_row.append(val)
        adj_mat.append(new_row)

    print("\n다익스트라 알고리즘으로 최단 경로 찾기")

    start_node_index = 0  # 'A' 정점에서 시작

    path, dist = shortest_path_dijkstra(vertex, adj_mat, start_node_index)

    print("\n[최단 경로 결과]")
    for end in range(len(vertex)):
        if end != start_node_index:
            # [최단경로: A->G] 출력
            print("[최단경로: %s->%s] %s" % (vertex[start_node_index], vertex[end], vertex[end]), end='')

            # 경로 역추적 (Backtracking)
            curr = end
            while path[curr] != start_node_index:
                print(" <- %s" % vertex[path[curr]], end='')
                curr = path[curr]

            # 시작 정점 출력
            print(" <- %s" % vertex[path[curr]])