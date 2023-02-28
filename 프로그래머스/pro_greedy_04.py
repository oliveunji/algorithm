def solution(people, limit):
    pair_count = 0
    people.sort()

    a = 0
    b = len(people)-1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            pair_count += 1
        b -= 1
    return len(people) - pair_count
