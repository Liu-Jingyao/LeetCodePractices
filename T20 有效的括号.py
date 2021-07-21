class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        barckets = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in barckets.keys():
                stk.append(c)
            elif not len(stk) or barckets[stk.pop()] != c:
                return False
        return not len(stk)


s = Solution()
while True:
    print(s.isValid(input()))
