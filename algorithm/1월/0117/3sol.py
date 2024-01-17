# Leetcode 179. Largest Number

class Solution:
    def __init__(self):
        self.sort_target = list()

    def str_sort(self):
        def bubble_sort(arr):
            n = len(arr)

            for i in range(n):
                for j in range(i + 1, n):
                    if int(arr[i] + arr[j]) < int(arr[j] + arr[i]):
                        arr[i], arr[j] = arr[j], arr[i]

        bubble_sort(self.sort_target)

    def largestNumber(self, nums: List[int]) -> str:
        for num in nums:
            self.sort_target.append(str(num))

        self.str_sort()

        answer = "".join(self.sort_target)
        answer = str(int(answer))
        return answer