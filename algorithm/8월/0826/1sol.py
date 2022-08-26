# set으로 받아서 철자를 다 없앤다.
# 백트래킹 돌려서 인지할 수 있는 것만 남김
# m이 5보다 작은 경우 anta tica 를 인지할 수 없어서 무조건 0을 print
# check 배열에 알파벳 넣었다가 시간초과 visit배열처럼 만들어줌
# 위에서 check배열을 visit처럼 만들어줘도 시간초과남 -> 조합처럼 뽑아주자
def solve(idx,num):
    global answer
    if idx == m-5:
        cnt = 0
        for w in words :
            flag = True
            for alph in w:
                if not check[ord(alph)-ord('a')]:
                    flag = False
                    break
            if flag :
                cnt += 1
        answer = max(answer,cnt)
        return
    else:
        for i in range(num,26):
            if not check[i]:
                check[i] = 1
                solve(idx+1,i)
                check[i] = 0
            pass

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
    solve(0,0)
    print(answer)
    pass
