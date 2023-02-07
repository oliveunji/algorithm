def solution(n, lost, reserve):
    lost_and_reserve = list(set(lost) & set(reserve))
    if lost_and_reserve != 0:
        for item in lost_and_reserve:
            lost.remove(item)
            reserve.remove(item)

    borrow_cnt = 0
    for item in lost:

        candidate1 = item - 1
        candidate2 = item+1
        if candidate1 in reserve:
            reserve.remove(candidate1)
            borrow_cnt += 1
        elif candidate2 in reserve:
            reserve.remove(candidate2)
            borrow_cnt += 1
        else:
            continue

    missing_cnt = len(lost) - borrow_cnt
    return n - missing_cnt
