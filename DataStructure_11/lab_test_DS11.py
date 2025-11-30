from my_complex_graph import vertex, weight
import Kruskal  # MSTKruskal 함수
import Prim  # MSTPrim 함수
import Dijkstra  # shortest_path_dijkstra 함수

def run_experiment():

    INF = 9999
    adj_mat_inf = []
    for row in weight:
        new_row = [INF if x is None else x for x in row]
        adj_mat_inf.append(new_row)

    print("\n[실험 1] Kruskal")
    Kruskal.MSTKruskal(vertex, weight)

    print("\n[실험 2] Prim")
    Prim.MSTPrim(vertex, weight)

    print("\n[실험 3] Dijkstra (Start: 0)")
    start_node = 0
    path, dist = Dijkstra.shortest_path_dijkstra(vertex, adj_mat_inf, start_node)

    print("\n0번 정점에서 각 정점까지의 최단 거리:")
    print(dist)

    target = 9
    print(f"\n[결과] 0번에서 {target}번까지의 최단 경로:")
    if dist[target] == INF:
        print("경로 없음")
    else:
        print(f"도착: {vertex[target]}", end="")
        curr = target
        while curr != start_node:
            curr = path[curr]
            print(f" <- {vertex[curr]}", end="")
        print(f" (비용: {dist[target]})")


if __name__ == "__main__":
    run_experiment()