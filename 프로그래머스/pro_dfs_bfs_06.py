import collections


def solution(tickets):
    answer = []

    dict = collections.defaultdict(list)
    for a, b in sorted(tickets, key=lambda x: (x[0], x[1])):
        dict[a].append(b)

    def dfs(s):
        while dict[s]:
            dfs(dict[s].pop(0))

        answer.append(s)
        return

    dfs("ICN")
    return answer[::-1]
