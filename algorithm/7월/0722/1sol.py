def solution(arr, divisor):
    answer = []
    for i in arr:
        if not i % divisor:
            answer.append(i)
    answer.sort()
    if not answer:
        answer.append(-1)

    return answer