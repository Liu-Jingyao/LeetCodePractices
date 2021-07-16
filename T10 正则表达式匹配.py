class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = " " + p
        s = " " + s
        p_len = len(p)
        s_len = len(s)
        dp = [[False for _ in p] for _ in s]

        dp[0][0] = True
        for p_i in range(2, p_len):
            if p[p_i] == '*':
                dp[0][p_i] = dp[0][p_i-2]

        for s_i in range(1, s_len):
            for p_i in range(1, p_len):
                if p[p_i] == '*':
                    # pi为*，可以匹配s中0-n个字符，分两种情况：
                    # 1. pi上一个字符和si不匹配，需要舍弃掉，因此匹配结果和pi上上个字符和si的结果一样
                    # 2. pi上一个字符和si匹配，保留，因此匹配结果和pi与si的上个字符匹配结果一样（'字符*'可能匹配s中的多个字符）
                    dp[s_i][p_i] = dp[s_i][p_i-2] or ((p[p_i-1] == '.' or p[p_i-1] == s[s_i]) and dp[s_i-1][p_i])
                else:
                    # pi不为*，只能匹配s中一个字符。如果pi不和si匹配直接为false, 否则为pi上个字符与si上个字符匹配的结果
                    dp[s_i][p_i] = (p[p_i] == '.' or p[p_i] == s[s_i]) and dp[s_i-1][p_i-1]

        return dp[s_len-1][p_len-1]


a = Solution()
while True:
    command = input()
    s_start = command.index('"', 0) + 1
    s_end = command.index('"', s_start + 1)
    s = command[s_start: s_end]
    p_start = command.index('"', s_end + 1) + 1
    p_end = command.index('"', p_start)
    p = command[p_start: p_end]
    print(a.isMatch(s, p))
