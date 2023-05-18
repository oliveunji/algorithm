import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    value = arr[0]
    count = 1

    for i in range(1, N):
        if arr[i] - value >= mid:
            count += 1
            value = arr[i]

    if count >= C:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
