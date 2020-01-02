def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i




input = [3, 0, 6, 1, 5]
result = solution(input)
print(result)