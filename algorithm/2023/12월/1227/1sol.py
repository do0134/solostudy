# 백준 1153 네 개의 소수

def make_pn(n):
    v = [0]*(n+1)
    value = list()

    for i in range(2,n+1):
        if not v[i]:
            v[i] = 1
            value.append(i)
            for j in range(i*2,n+1,i):
                v[j] = 1

    return value


def solve(prime_number, n):
    if n % 2:
        n -= 5
        answer = [2,3]
    else:
        n -= 4
        answer = [2,2]
    L = len(prime_number)
    l = 0
    r = L -1
    v = list()

    while l <= r:
        if prime_number[l]+prime_number[r] > n:
            r -= 1
        elif prime_number[l]+prime_number[r] < n:
            l += 1
        else:
            v = [prime_number[l],prime_number[r]]
            answer += v
            return answer
    if not v:
        return [-1]
    else:
        return answer + v


N = int(input())
pn = make_pn(N)
answer_list = solve(pn, N)
if len(answer_list) != 4:
    print(-1)
else:
    print(*sorted(answer_list))
