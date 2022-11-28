class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        v = [0] * 100001

        for i in matches:
            if v[i[0]] == 0:
                v[i[0]] = -1

            if v[i[1]] == -1:
                v[i[1]] = 1

            else:
                v[i[1]] += 1

        v1 = list()
        v2 = list()

        for i in range(100001):
            if v[i] == -1:
                v1.append(i)
            if v[i] == 1:
                v2.append(i)

        return [v1, v2]