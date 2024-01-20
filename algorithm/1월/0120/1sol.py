# Leetcode 743. Network Delay Time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = list()
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((w, v))

        dp = [int(1e9)] * (n + 1)
        dp[k] = 0
        dp[0] = 0

        heappush(heap, (0, k))
        cnt = 1

        while heap:
            now_w, now_idx = heappop(heap)

            for next_w, next_idx in graph[now_idx]:
                if dp[next_idx] > now_w + next_w:
                    if dp[next_idx] == int(1e9):
                        cnt += 1
                    dp[next_idx] = now_w + next_w
                    heappush(heap, (now_w + next_w, next_idx))

        if cnt == n:
            return max(dp)

        return -1
