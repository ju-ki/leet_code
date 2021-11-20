class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(str(x)[::-1])
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


# Runtime: 68 ms, faster than 49.40 % of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.1 MB, less than 93.07 % of Python3 online submissions for Palindrome


if __name__ == "__main__":
    solution = Solution()
    x = 121
    print(solution.isPalindrome(x=x))
