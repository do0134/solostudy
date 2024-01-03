def shuffle():
    card_list = [0]*n

    for i in range(n):
        card_list[s[i]] = card[i]

    return card_list


n = int(input())
p = list(map(int,input().split()))
s = list(map(int,input().split()))
card = [i for i in range(n)]
fail = [i for i in range(n)]
answer = 0

while True:
    for i,j in enumerate(card):
        if p[j] != i%3:
            break
    else:
        print(answer)
        break

    if answer and card == fail:
        print(-1)
        break

    card = shuffle()
    answer += 1
