from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        min_i = 3E4
        max_i = 0
        max_a = 0
        # 将坐标，高度封装为元组
        i_height = enumerate(height)
        # 从高到低遍历每个点，考察每条高度线上的最大面积。
        i_height = sorted(i_height, key=lambda a: a[1], reverse=True)
        for i, h in i_height:
            # 如果上一个最左端的点（同高度或更高）比当前点还靠左，那么当前高度最左端的还是上一个点，否则是当前点。
            min_i = min(i, min_i)
            # 同理，计算当前高度最右端的点。
            max_i = max(i, max_i)
            # 得到高度线下的最大的面积
            max_a = max(max_a, h * (max_i - min_i))
        # 需要每个点遍历一次，时间复杂度O(n), 总体时间复杂度是排序的O(nlogn)
        return max_a


s = Solution()
while True:
    height = eval(input())
    print(s.maxArea(height))