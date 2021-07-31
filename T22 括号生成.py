from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.res = set()
        self.dfs(n-1, 1)
        res_list = sorted(list(self.res))
        str_list = []
        for num in res_list:
            bin_str = bin(num)[2:].rjust(self.n << 1, '0')
            res_str = "".join(['(' if bit == '0' else ')' for bit in bin_str])
            str_list.append(res_str)
        return str_list

    def dfs(self, k, num):
        if not k:
            if num not in self.res:
                self.res.add(num)
            return
        self.dfs(k-1, num | 1 << ((self.n-k) << 1))
        self.dfs(k-1, num << 1 | 1)
        self.dfs(k-1, num << 2 | 1)

while True:
    s = Solution()
    print(s.generateParenthesis(int(input())))