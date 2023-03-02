from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 0
    arr = [0 for _ in range(bridge_length)]
    bridge = deque(arr)
    while bridge:
        answer += 1
        bridge.popleft()

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
            else:
                bridge.append(0)
    return answer


solution(2, 10, [7, 4, 5, 6])
