# Leetcode 46. Permutations
# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = list()

        # for i in permutations(nums, len(nums)):
        #     answer.append(i)

        # return answer

        q = deque()
        n = len(nums)

        for i in range(n):
            temp = set()
            temp.add(i)
            q.append(([nums[i]], temp))

        while q:
            now, v = q.popleft()

            if len(v) >= n:
                answer.append(now)
            else:
                for i in range(n):
                    if i not in v:
                        v.add(i)
                        q.append((now + [nums[i]], copy.deepcopy(v)))
                        v.remove(i)

        return answer