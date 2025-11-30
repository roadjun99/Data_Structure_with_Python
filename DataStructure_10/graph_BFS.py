from queue import Queue
from my_graph import edges, num_vertices, print_adjacency_matrix

def BFS_AdjMatrix(vtx, adj, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True

    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')

        for v in range(n):
            if adj[s][v] != 0:
                if visited[v] == False:
                    Q.put(v)
                    visited[v] = True

if __name__ == "__main__":
    print("\nBFS 테스트")
    vtx = [i for i in range(num_vertices)]

    adj_matrix = print_adjacency_matrix(num_vertices, edges)

    print('\nBFS(출발:0): ', end="")

    BFS_AdjMatrix(vtx, adj_matrix, 0)
    print()