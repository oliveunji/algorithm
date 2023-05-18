import collections
def solution(genres, plays):
    g_list = collections.defaultdict(list)
    g_count = collections.defaultdict(int)
    
    for i, (genre, count) in enumerate(zip(genres, plays)):
        g_list[genre].append((i, count))
        g_count[genre] += count
    
    answer = []
    for k,y in sorted(g_count.items(), key=lambda x:x[1], reverse=True):
        for i, val in sorted(g_list[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"],
         [500, 600, 150, 800, 2500])
