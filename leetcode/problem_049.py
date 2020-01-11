'''
Group Anagrams
https://leetcod e.com/problems/group-anagrams/
'''


def solution(strs):

    d = {}
    for w in strs:
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return list(d.values())


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution(input))
