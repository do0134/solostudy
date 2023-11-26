# 백준 1148 단어 만들기

from collections import defaultdict

my_dict = list()

while True:
    s = input()
    if s == "-":
        break
    else:
        my_dict.append(s)

while True:
    s = input()
    if s == "#":
        break
    puzzle = defaultdict(int)
    used = defaultdict(int)

    for i in s:
        puzzle[i] += 1

    for word in my_dict:
        for w in set(word):
            if not puzzle[w] or word.count(w) > puzzle[w]:
                break
        else:
            for w in set(word):
                used[w] += 1

    min_v = [int(1e9), ""]
    max_v = [0, ""]

    for key in sorted(puzzle.keys()):
        if puzzle[key]:
            if used[key] == min_v[0]:
                min_v[1] += key
            elif used[key] < min_v[0]:
                min_v[0] = used[key]
                min_v[1] = key

            if used[key] > max_v[0]:
                max_v[0] = used[key]
                max_v[1] = key
            elif used[key] == max_v[0]:
                max_v[1] += key


    print(min_v[1] ,min_v[0], max_v[1], max_v[0])