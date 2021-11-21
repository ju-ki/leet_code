class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# Runtime: 31 ms, faster than 59.37 % of Python3 online submissions for Length of Last Word.
# Memory Usage: 14.1 MB, less than 87.96 % of Python3 online submissions for Length of Last Word.


if __name__ == "__main__":
    s = "Hello jukiya"
    solution = Solution()
    print(solution.lengthOfLastWord(s))
