from queue import Queue
from my_graph import edges, num_vertices, print_adjacency_matrix

def ST_BFS(vtx, adj, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        s = Q.get()

        for v in range(n):
            if adj[s][v] != 0:
                if visited[v] == False:

                    print("(", vtx[s], vtx[v], ")", end=' ')

                    Q.put(v)
                    visited[v] = True

if __name__ == "__main__":
    print("\n신장 트리 테스트")
    vtx = [i for i in range(num_vertices)]
    adj_matrix = print_adjacency_matrix(num_vertices, edges)

    print('\n신장트리(BFS): ', end="")
    ST_BFS(vtx, adj_matrix, 0)
    print()