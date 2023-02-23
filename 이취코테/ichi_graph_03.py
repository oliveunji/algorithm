N, M = map(int, input().split())
graph = []


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * (N)
for i in range(N):
    parent[i] = i

edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

total_cost = 0
edges.sort()
min_cost = 0
for edge in edges:
    cost, a, b = edge
    total_cost += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost
print(total_cost - min_cost)
