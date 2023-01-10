# leetcode 739. Daily Temperatures
# 무게 싣는 문제나, 시간 가르는 문제처럼 뒤에서 반복문 돌아서, 누적합을 구하면 훨씬 효율적으로 풀수 있다.... 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures[::]
        n = len(t)
        answer = [0]*n
        dp = [[] for _ in range(101)]
        num = 0
        
        for i in range(n) :
            dp[t[i]].append(i)
            num += 1
            if num == 1 :
                continue
            for j in range(30,t[i]) :
                if not dp[j] :
                    continue
                for p in dp[j] :
                    answer[p] = i-p
                    num -= 1
                dp[j] = []
                if num == 1 :
                    break

        return answer