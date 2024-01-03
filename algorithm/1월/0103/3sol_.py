from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        def make_num_dict(arr: list[int]):
            if not arr:
                return

            one_num = positive_one_num
            two_num = positive_two_num

            for i in range(len(arr)):
                one_num[arr[i]] = True
                for j in range(i + 1, len(arr)):
                    two_num[arr[i] + arr[j]].add((min(arr[i], arr[j]), max(arr[i], arr[j])))

        def check_3sum(arr: list):
            for i in range(len(arr)):
                if not negative_one_num1[arr[i]] and zeros and positive_one_num[-arr[i]]:
                    answer.add(tuple(sorted((arr[i], 0, -arr[i]))))
                    negative_one_num1[arr[i]] = True

                if not negative_one_num2[arr[i]] and positive_two_num[-arr[i]]:
                    for value1, value2 in positive_two_num[-arr[i]]:
                        answer.add(tuple(sorted(arr[i], value1, value2)))
                    negative_one_num2[arr[i]] = True

                for j in range(i + 1, len(arr)):
                    value = arr[i] + arr[j]
                    if positive_one_num[-value]:
                        answer.add(tuple(sorted(arr[i], arr[j], -value)))

                    negative_two_num[(min(arr[i], arr[j]), max(arr[i], arr[j]))] = True

        negative = list()
        zeros = list()
        positive = list()

        for num in nums:
            if num < 0:
                negative.append(num)
            elif num > 0:
                positive.append(num)
            else:
                zeros.append(num)

        answer = set

        if len(zeros) >= 3:
            answer.append([0, 0, 0])

        negative_one_num1 = defaultdict(bool)
        negative_one_num2 = defaultdict(bool)
        negative_two_num = defaultdict(bool)

        positive_one_num = defaultdict(bool)
        positive_two_num = defaultdict(set)

        make_num_dict(positive)

        check_3sum(negative)

        return answer


"""
-2 0 1 1 2
3 0 -2 -1 1 2
"""