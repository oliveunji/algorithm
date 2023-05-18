def make_trie(words, reverse):
    dic = {}
    for word in words:
        dic.setdefault(len(word), {})
        current_dic = dic[len(word)]

        if reverse:
            word = word[::-1]

        for letter in word:
            current_dic.setdefault(letter, [0, {}])
            current_dic[letter][0] += 1
            current_dic = current_dic[letter][1]

        return dic


def count(query, new_query, cur_dic):
    if len(query) not in cur_dic.keys():
        return 0
    current_dic = cur_dic[len(query)]
    for letter in new_query:
        if letter not in current_dic.keys():
            return 0
        current_dic = current_dic[letter][1]


def solution(words, queries):
    answer = []
    dic = make_trie(words, False)
    reverse_dic = make_trie(words, True)

    for query in queries:
        new_query = query.replace("?", "")
        if query[0] == "?":
            temp = count(query, new_query[::-1], reverse_dic)
            answer.append(temp)
        else:
            temp = count(query, new_query, dic)
            answer.append(temp)

    return answer
