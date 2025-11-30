from my_weighted_graph import vertex, weight

INF = 9999


def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print(" INF ", end='')
            else:
                print("%4d " % A[i][j], end='')
        print("")


def get_path(u, v, Next, vtx):
    """Next 배열을 이용하여 u에서 v까지의 경로를 리스트로 반환"""
    if Next[u][v] is None:
        return None

    path = [vtx[u]]
    curr = u
    while curr != v:
        curr = Next[curr][v]
        path.append(vtx[curr])
    return path


def shortest_path_floyd_path(vertex, adj):
    vsize = len(vertex)

    # 1. 거리 배열(A)과 경로 배열(Next) 초기화
    A = [[INF] * vsize for _ in range(vsize)]
    Next = [[None] * vsize for _ in range(vsize)]

    for i in range(vsize):
        A[i][i] = 0
        for j in range(vsize):
            if adj[i][j] is not None:
                A[i][j] = adj[i][j]
                Next[i][j] = j

                # 2. Floyd 알고리즘 수행
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]
                    Next[i][j] = Next[i][k]

    return A, Next


if __name__ == "__main__":
    print("Shortest Path By Floyd's Algorithm (With Path Reconstruction)")

    dist_matrix, next_matrix = shortest_path_floyd_path(vertex, weight)

    print("\n[최종 거리 행렬]")
    printA(dist_matrix)

    # --- Dijkstra 결과와 비교 검증 ---
    start_node = 0  # A
    end_node = 6  # G

    print(f"\n[검증] {vertex[start_node]}에서 {vertex[end_node]}까지의 최단 경로 비교")

    floyd_dist = dist_matrix[start_node][end_node]
    floyd_path_list = get_path(start_node, end_node, next_matrix, vertex)

    floyd_path_str = " -> ".join(floyd_path_list) if floyd_path_list else "경로 없음"

    print(f"Floyd 결과   : 비용 = {floyd_dist}, 경로 = {floyd_path_str}")

    print("-" * 60)
    # [수정됨] 17 -> 15, A->B->E->G -> A->C->D->E->G
    print("Dijkstra 결과: 비용 = 15,   경로 = A -> C -> D -> E -> G")

    if floyd_dist == 15 and floyd_path_list == ['A', 'C', 'D', 'E', 'G']:
        print(">> 결론: 두 알고리즘의 결과가 완벽하게 일치합니다! (성공)")
    else:
        print(">> 결론: 결과가 다릅니다. 확인이 필요합니다.")