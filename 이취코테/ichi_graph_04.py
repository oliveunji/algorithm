N = int(input())
arr = []
for _ in range(N):
    x, y, z = map(int, input().split())
    arr.append((x, y, z))


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


# for x, y, z in arr:


def calc_distance(point1, point2):
    diff_x = abs(point1.x - point2.x)
    diff_y = abs(point1.y - point2.y)
    diff_z = abs(point1.z - point2.z)
    return min(diff_x, diff_y, diff_z)
