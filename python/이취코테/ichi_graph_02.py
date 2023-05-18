G = int(input())  # 탑승구의 갯수
P = int(input())  # 비행기 입력 갯수


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


parent = [0] * (G+1)
for i in range(1, G+1):
    parent[i] = i

result = 0
for _ in range(P):
    root = find_parent(parent, int(input()))
    if root == 0:
        break
    union_parent(parent, root, root-1)
    result += 1

print(result)
