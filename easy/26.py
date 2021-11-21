from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # index_unique = 1
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[index_unique] = nums[i]
        #         index_unique += 1
        index_unique = len(set(nums))

        return index_unique


if __name__ == "__main__":
    nums = [1, 1, 2]
    solution = Solution()
    print(solution.removeDuplicates(nums=nums))
