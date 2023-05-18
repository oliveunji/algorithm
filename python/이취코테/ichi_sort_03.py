import collections


def solution(N, stages):
    failure = collections.defaultdict(float)
    length = len(stages)

    prev_count = 0
    for i in range(1, N+1):
        if length != 0:

            stage_count = stages.count(i)
            failure[i] = stage_count / length
            length -= stage_count
        else:
            failure[i] = 0

    answer = sorted(failure.keys(), key=lambda key: failure[key], reverse=True)

    return answer
