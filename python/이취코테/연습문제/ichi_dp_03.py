# import math


# def solution(N, K):
#     root_val = math.sqrt(N)
#     if root_val ** 2 == N:
#         return 2
#     else:
#         return N - (root_val ** 2)


# print(solution(25, 5))


n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)
