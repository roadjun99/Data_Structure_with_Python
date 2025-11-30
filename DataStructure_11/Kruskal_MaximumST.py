from my_weighted_graph import vertex, weight

parent = []
set_size = 0

def init_set(nSets):
    global set_size, parent
    set_size = nSets
    parent = []
    for i in range(nSets):
        parent.append(-1)

def find(id):
    while (parent[id] >= 0):
        id = parent[id]
    return id

def union(s1, s2):
    global set_size
    parent[s1] = s2
    set_size = set_size - 1

# MSTKruskal 수정
def MSTKruskal(vertex, adj):
    vsize = len(vertex)
    init_set(vsize)
    eList = []

    # 모든 간선들 리스트에 넣기
    for i in range(vsize - 1):
        for j in range(i + 1, vsize):
            if adj[i][j] is not None:
                eList.append((i, j, adj[i][j]))

    # 가중치 기준으로 간선 내림차순 정렬 (pop(-1) 최대가 되도록)
    eList.sort(key=lambda e: e[2], reverse=True)

    edgeAccepted = 0
    mst_weight_sum = 0  # 가중치 합 저장할 변수

    print("\nKruskal 알고리즘: 최대 비용 신장 트리 구하기")

    while (edgeAccepted < vsize - 1):
        if not eList:  # 간선 부족 시
            break

        e = eList.pop(0)  # 과제 해결 부분. 가장 큰 가중치를 가진 간선.
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset:  # 사이클이 생기지 않으면
            print("간선 추가 : (%s, %s, %d)" % (vertex[e[0]], vertex[e[1]], e[2]))

            union(uset, vset)  # 합치기
            edgeAccepted += 1
            mst_weight_sum += e[2]  # 가중치 누적

    # 최종 가중치 합
    print(f"\nMST의 가중치 합 (Total Weight): {mst_weight_sum}")


if __name__ == "__main__":
    MSTKruskal(vertex, weight)