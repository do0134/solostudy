# 이건 메모리초과 나는 코드

from itertools import combinations
n,m = map(int,input().split())
check = [0]*26
answer = 0
words = [set(input()) for _ in range(n)]
if m < 5 :
    print(0)
elif m == 26:
    print(n)
else:
    for i in ['a','n','t','i','c']:
        check[ord(i)-ord('a')] = 1
    comb = list(combinations([i for i in range(26)],m-5))
    for c in comb :
        cnt = 0
        temp = check[::]
        for num in c:
            temp[num] = 1
        for w in words :
            flag = True
            for alpha in w:
                if not temp[ord(alpha)-97]:
                    flag = False
                    break
            if flag :
                cnt += 1
        answer += cnt
    print(answer)
    pass