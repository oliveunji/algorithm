from itertools import permutations


def solution(k, dungeons):
    N = len(dungeons)
    route_list = list(permutations(dungeons, N))
    # results = []
    answer = 0
    for i, item in enumerate(route_list):
        remain = k
        count = 0
        for a, b in item:
            if remain < a:
                break
            else:
                remain -= b
            count += 1
        # results.append(count)
        if count > answer:
            answer = count
    # print(results)

    # answer = -1
    return answer


solution(80, [[80, 20], [50, 40], [30, 10]])
