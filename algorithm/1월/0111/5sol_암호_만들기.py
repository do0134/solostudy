# 백준 1759 암호 만들기
# https://www.acmicpc.net/problem/1759

from itertools import combinations

l,c = map(int,input().split())
arr = list(input().split(" "))
arr.sort()

for combi in combinations(arr,l):
    consonant = 0
    vowel = 0
    for s in combi:
        if s in "aeiou":
            vowel += 1
        else:
            consonant += 1
    if consonant >= 2 and vowel >= 1:
        print("".join(combi))