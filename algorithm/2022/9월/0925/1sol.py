# 순열뽑기
# 사전순으로 뽑아야하기 때문에 정렬한 다음, 백트래킹
# permutation 함수를 써도 되지만....
def perm(per,idx):
    if idx == m:
        print(*per)
        return
    else:
        for i in range(n):
            if not v[i]:
                v[i] = 1
                per.append(arr[i])
                perm(per,idx+1)
                per.pop()
                v[i] = 0
            pass


n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
v = [0]*n
perm([],0)
