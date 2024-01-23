# 백준 1461 도서관

n,m = map(int,input().split())
arr = list(map(int,input().split()))

negative = list()
positive = list()

for i in arr:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)


if not negative:
    negative.append(0)

if not positive:
    positive.append(0)

negative.sort()
positive.sort(reverse=True)

answer = 0


def check_walk(book_list):
    global answer

    l = len(book_list)

    for i in range(0, l, m):
        prev = book_list[i]
        answer += abs(book_list[i])*2
        for j in range(i+1, min(l, i+m)):
            prev = book_list[j]


if max(positive) > abs(min(negative)):
    check_walk(negative)
    check_walk(positive)
    answer -= max(positive)
else:
    check_walk(positive)
    check_walk(negative)
    answer -= abs(min(negative))

print(answer)