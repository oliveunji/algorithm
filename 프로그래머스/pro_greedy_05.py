def solution(n, costs):
    # 크루스칼 알고리즘

    def find_parent(parent, a):
        if parent[a] != a:
            parent[a] = find_parent(parent, parent[a])
        return parent[a]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [0] * (n)
    for i in range(n):
        parent[i] = i

    edges = []
    for i, j, cost in costs:
        edges.append((cost, i, j))
    edges.sort()

    answer = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer
