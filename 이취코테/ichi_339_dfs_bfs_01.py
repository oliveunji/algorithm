def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def distance_count(input):
    input_arr = input.split("\n")
    values = list(map(int, input_arr[0].split()))
    N = values[0]
    K = values[2]
    X = values[3]  # start node

    distance_arr = []
    for item in input_arr[1:]:
        distance_arr.append(list(map(int, item.split())))
    # print(distance_arr, K, X)

    visited = [False] * (N+1)
    graph = [[] for _ in range(N+1)]
    for a, b in distance_arr:
        graph[a].append(b)
    # print(graph)
    dfs(graph, visited, X)


input = """4 4 2 1
1 2
1 3
2 3
2 4"""

expected_output = 4

distance_count(input)
