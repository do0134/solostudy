# Leetcode 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero = list()
        one = list()
        two = list()

        for num in nums:
            if not num:
                zero.append(num)
            elif num == 1:
                one.append(num)
            else:
                two.append(num)

        nums[:] = zero + one + two

        # def quick_sort(arr):
        #     if not arr or len(arr) == 1:
        #         return arr

        #     pivot = arr[len(arr)//2]
        #     left = list()
        #     right = list()
        #     mid = list()

        #     for i in arr:
        #         if i > pivot:
        #             right.append(i)
        #         elif i < pivot:
        #             left.append(i)
        #         else:
        #             mid.append(i)

        #     return quick_sort(left) + mid + quick_sort(right)

        # nums[:] = quick_sort(nums)