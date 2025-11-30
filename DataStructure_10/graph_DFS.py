from my_graph import edges, num_vertices, print_adjacency_list

def DFS_AdjList(vtx, aList, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True

    for v in aList[s]:
        if visited[v] == False:
            DFS_AdjList(vtx, aList, v, visited)

if __name__ == "__main__":
    print("\nDFS 테스트")
    vtx = [i for i in range(num_vertices)]

    adj_dict = print_adjacency_list(num_vertices, edges)
    aList = [adj_dict[i] for i in range(num_vertices)]

    print('\nDFS(출발:0) : ', end="")

    DFS_AdjList(vtx, aList, 0, [False] * len(vtx))
    print()