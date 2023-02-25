import collections


def solution(participant, completion):
    dict = collections.Counter(participant)
    for name in completion:
        dict[name] -= 1

    for name, count in dict.items():
        if count != 0:
            return name
