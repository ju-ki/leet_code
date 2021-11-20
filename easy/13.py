class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        for i in s[::-1]:          # rev the s
            if dict[i] >= prev:
                # sum the value iff previous value same or more
                res += dict[i]
            else:
                # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
                res -= dict[i]
            prev = dict[i]
        return res

# Runtime: 72 ms, faster than 15.47 % of Python3 online submissions for Roman to Integer.
# Memory Usage: 14.2 MB, less than 84.39 % of Python3 online submissions for Roman to


if __name__ == "__main__":
    s = "IV"
    solution = Solution()
    print(solution.romanToInt(s))
