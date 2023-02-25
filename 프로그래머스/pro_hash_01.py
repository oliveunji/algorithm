import collections


def solution(nums):
    dict = collections.Counter(nums)
    max_val = len(nums) // 2
    key_length = len(dict.keys())
    if key_length > max_val:
        return max_val
    else:
        return key_length
