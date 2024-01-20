# Leetcode 787. Cheapest Flights Within K Stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [int(1e9)] * n
        airport = [[] for _ in range(n)]

        for u, v, w in flights:
            airport[u].append((w, v))

        q = deque()
        q.append((src, 0, -1))
        dp[src] = 0
        answer = int(1e9)

        while q:
            c_place, c_cost, c_move = q.popleft()
            if c_move > k:
                continue

            if c_place == dst and c_cost < answer:
                answer = c_cost
                continue
            for n_cost, n_place in airport[c_place]:
                if dp[n_place] > n_cost + c_cost:
                    q.append((n_place, c_cost + n_cost, c_move + 1))
                    dp[n_place] = n_cost + c_cost

        if answer == int(1e9):
            return -1

        return answer