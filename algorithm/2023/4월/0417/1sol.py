# 프로그래머스 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = list()
    for i,n in enumerate(numbers) :
        while stack and numbers[stack[-1]] < n :
            answer[stack.pop()] = n
        stack.append(i)
    return answer