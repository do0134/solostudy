n = int(input())

for _ in range(n):
    s = input()
    check = [0]*len(s)
    answer = 0
    if s[0] == 'O':
        check[0] = 1
        answer += 1
    for j in range(1,len(s)):
        if s[j] == 'O':
            if check[j-1] > 0 :
                check[j] += check[j-1]+1
            else:
                check[j] = 1
            answer += check[j]

    print(answer)


