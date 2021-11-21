# Create a dictionary for O(1) lookup.
# Create stack and add open braces on the top. If closing braces are encountered, then pop from stack and compare it's closing brace with the encountered brace.
# If closing brace is encountered but the stack is empty, then there's no matching pair for it. Hence return False.
# At the end, we want to make sure our stack is empty after all the matching pairs are found. If stack is not empty, return False.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_str = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in dict_str:
                stack.append(dict_str[i])
            # ([)]のようなパターンだとstack[-1]した際に一致しない
            elif len(stack) > 0 and i == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


# Runtime: 35 ms, faster than 31.22 % of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.2 MB, less than 65.38 % of Python3 online submissions for Valid

if __name__ == "__main__":
    s = "([)]"
    solution = Solution()
    print(solution.isValid(s))
