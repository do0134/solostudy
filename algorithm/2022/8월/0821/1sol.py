# 버블 소트 몇 번만에 소팅이 완료되는가 물어보는 문제
# 받을 때 인덱스 구해서 정렬한 다음, 원래 인덱스와 비교하면 됨
# 버블 소트 그대로 쓰면 최대 500,000이기 때문에 시간초과남
# 정렬 문제이지만 그냥 파이썬 내장 sort 알고리즘은 팀 소트이니 그냥 이걸 활용하자.
n= int(input())

arr = []

for i in range(n):
    arr.append([int(input()), i])

arr1 = sorted(arr)
answer = 0

for i in range(n):
    answer = max(answer,arr1[i][1]-arr[i][1]+1)

print(answer)


