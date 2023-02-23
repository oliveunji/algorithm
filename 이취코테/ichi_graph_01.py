N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))


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


parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

result = 'YES'
prev = find_parent(parent, plan[0])
for i in range(1, len(plan)):
    cur = find_parent(parent, plan[i])
    if prev != cur:
        result = 'NO'
        break
    else:
        prev = cur

print(result)
