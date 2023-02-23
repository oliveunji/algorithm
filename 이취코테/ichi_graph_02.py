G = int(input())
P = int(input())

arr = []
visited = [False] * P
for _ in range(P):
    arr.append(int(input()))

count = 0
for idx, val in enumerate(arr):
    flag = False
    for i in range(val-1, -1, -1):
        if visited[i] == False:
            visited[i] = True
            flag = True
            break
    if flag == False:
        break
    count += 1

print(count)
