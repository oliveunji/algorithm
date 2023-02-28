import collections
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr_count = list(collections.Counter(arr).items())

result = 0
for i in range(len(arr_count) - 1):
    for j in range(i+1, len(arr_count)):
        result += arr_count[i][1] * arr_count[j][1]

print(result)

# 5 3
# 1 3 2 3 2

# 8 5
# 1 5 4 3 2 4 5 2