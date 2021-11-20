
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix

# Runtime 46 ms


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest


# Runtime: 43 ms, faster than 27.09 % of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.4 MB, less than 25.70 % of Python3 online submissions for Longest


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs=strs))
