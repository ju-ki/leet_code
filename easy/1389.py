from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        len_numbers = len(nums)
        for i in range(len_numbers):
            target.insert(index[i], nums[i])

        return target


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, n in zip(index, nums):
            target.insert(i, n)

        return target


# Runtime: 32 ms, faster than 80.90 % of Python3 online submissions for Create Target Array in the Given Order.
# Memory Usage: 14.3 MB, less than 51.30 % of Python3 online submissions for Create Target Array in the Given Order.


if __name__ == "__main__":
    nums, index = [0, 1, 2, 3, 4], [0, 1, 2, 2, 1]
    solution = Solution()
    print(solution.createTargetArray(nums, index))
