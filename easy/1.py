from typing import List
import random


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_numbers = len(nums)
        index = []
        for i in range(len_numbers):
            j = i + 1
            while j < len_numbers:
                summation = nums[i] + nums[j]
                if summation == target:
                    index.append(i)
                    index.append(j)
                    break
                j += 1
        return index

# Runtime: 6708 ms, faster than 7.27 % of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 64.98 % of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            # print(n)
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i


# Runtime: 64 ms, faster than 60.71 % of Python3 online submissions for Two Sum.
# Memory Usage: 15.7 MB, less than 8.84 % of Python3 online submissions for Two Sum.


if __name__ == "__main__":
    nums = [2, 3, 4, 5]
    target = 8
    solution = Solution()
    print(solution.twoSum(nums=nums, target=target))
