n = int(input())

arr = [0] * n
arr[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    val = min(next2, next3, next5)
    arr[i] = val
    if val == next2:
        i2 += 1
        next2 = arr[i2] * 2

    if val == next3:
        i3 += 1
        next3 = arr[i3] * 3

    if val == next5:
        i5 += 1
        next5 = arr[i5] * 5

print(arr[-1])
