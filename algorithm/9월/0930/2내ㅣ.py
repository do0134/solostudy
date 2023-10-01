from collections import defaultdict

n = int(input())
trie = defaultdict(defaultdict)
keys = list()
for _ in range(n):
    s = input()
    keys.append(s)
    trie[s] = defaultdict(int)
    for char in s:
        trie[s][char] += 1

answer = 0
same = list()
for i in range(1,n):
    if trie[keys[i]] == trie[keys[0]]:
        answer += 1

print(answer)