from collections import defaultdict


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose = defaultdict(int)
        player = set()

        for i, j in matches:
            player.add(i)
            player.add(j)
            lose[j] += 1

        answer1 = list()
        answer2 = list()

        for i in sorted(player):
            if lose[i] == 0:
                answer1.append(i)
            elif lose[i] == 1:
                answer2.append(i)
        return [answer1, answer2]
