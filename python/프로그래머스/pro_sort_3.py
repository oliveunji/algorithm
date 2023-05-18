def solution(citations):
    citations.sort()
    length = len(citations)
    h_idx = 0
    for idx, val in enumerate(citations):
        cur_h_idx = min(val, length - idx)
        h_idx = max(cur_h_idx, h_idx)
    return h_idx
