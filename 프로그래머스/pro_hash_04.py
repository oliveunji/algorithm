import collections


def solution(clothes):
    dict = collections.defaultdict(list)
    for item, item_type in clothes:
        dict[item_type].append(item)

    total_select_count = 1
    for item in dict:
        total_select_count *= (len(dict[item])+1)
    return total_select_count - 1
