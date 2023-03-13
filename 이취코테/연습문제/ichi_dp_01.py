import collections


def solutions(M, K, arr):
    key_list = sorted(arr)
    k1 = key_list[-1]
    k2 = key_list[-2]

    result = 0
    while True:
        for _ in range(K):
            if M == 0:
                break
            result += k1
            M -= 1
        if M == 0:
            break
        result += k2
        M -= 1

    print(result)


solutions(8, 3, [2, 4, 5, 4, 6])

# 어려웠던점.
# 1. 같은수가 중복될 수 도 있는데, 그거 상관없이 sort 한 후에 위에서부터 차례대로 자르면 되는 것 이었다.
# 2. 수를 더할때 m값을 기준으로 그 값을 빼주면서 계속 더해주면 되었다...
# 답을 보면 간단하지만 혼자 생각하려면 묘하게 어려운 문제였다. 
