class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        flag = [False for _ in s]
        max_len = 0
        for i, c in enumerate(s):
            if stk and stk[-1][1] == '(' and c == ')':
                flag[stk[-1][0]] = flag[i] = True
                stk.pop()
            else:
                stk.append((i, c))

        tmp_len = 0
        for f in flag:
            if f:
                tmp_len += 1
            else:
                max_len = max(tmp_len, max_len)
                tmp_len = 0
        else:
            max_len = max(tmp_len, max_len)
        return max_len

    def isValid(self, s):
        stk = []
        for c in s:
            if stk[-1] == '(' and c == ')':
                stk.pop()
            else:
                stk.append(c)
        return not stk


s = Solution()
while True:
    inp = input()
    print(s.longestValidParentheses(inp))