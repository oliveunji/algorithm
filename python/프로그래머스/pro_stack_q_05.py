from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    now = sum(bridge)
    time = 0

    while bridge:
        time += 1
        now -= bridge.popleft()

        if truck_weights:
            if now + truck_weights[0] <= weight:
                bridge.append(truck_weights[0])
                now += truck_weights.popleft()
            else:
                bridge.append(0)

    return time
