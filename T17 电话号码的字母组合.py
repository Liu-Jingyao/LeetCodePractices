from typing import List


class Solution:
    result = []
    l = [None, None,
         set({'a', 'b', 'c'}),
         set({'d', 'e', 'f'}),
         set({'g', 'h', 'i'}),
         set({'j', 'k', 'l'}),
         set({'m', 'n', 'o'}),
         set({'p', 'q', 'r', 's'}),
         set({'t', 'u', 'v'}),
         set({'w', 'x', 'y', 'z'})]

    def letterCombinations(self, digits: str) -> List[str]:
        Solution.result = []
        self.makeWord(digits, "")
        return Solution.result

    def makeWord(self, digits, word):
        if digits == "":
            if word != "":
                Solution.result.append(word)
            return
        for c in Solution.l[int(digits[0:1])]:
            self.makeWord(digits[1:], word+c)

s = Solution()
while True:
    print(s.letterCombinations(input()))