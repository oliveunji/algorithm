n = int(input())

ugly = [0] * n
ugly[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])


# N = int(input())
# # num = [2, 3, 5]
# arr = [2, 3, 5]

# count = 1
# while count > N:
#     for i in range(len(arr)):
#         arr.append(arr[i]*arr[i])
#         arr.append(arr[i]*arr[i+1])
#         arr.append(arr[i]*arr[i+2])
#         count += 3
# arr.sort()
# print(arr[n+1])
