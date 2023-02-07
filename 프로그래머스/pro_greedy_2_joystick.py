def solution(name):
    diff_arr = []
    zero_indexes = []
    for idx, char in enumerate(list(name)):
        min_diff = min(ord(char)-ord('A'), ord('Z')-ord(char)+1)
        if min_diff == 0:
            zero_indexes.append(idx)
        diff_arr.append(min_diff)

    if len(zero_indexes) == 0:
        return sum(diff_arr) + len(diff_arr) - 1
    else:
        max_gap = 0
        for idx in range(len(zero_indexes)-1):
            cur_gap = 0
            if zero_indexes[idx] + 1 == zero_indexes[idx+1]:
                cur_gap += 1
            max_gap = max(cur_gap, max_gap)
        if len(diff_arr) - max_gap < max_gap:
            return sum(diff_arr) + len(diff_arr) - max_gap
        else:
            return sum(diff_arr) + max_gap

# reference - https://100winone.tistory.com/81
