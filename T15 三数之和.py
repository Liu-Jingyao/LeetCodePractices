from typing import List


class Solution:
    def __binarySearch(self, arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.__binarySearch(arr, l, mid - 1, x)
            else:
                return self.__binarySearch(arr, mid + 1, r, x)
        else:
            return -1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        nlen = len(nums)
        for i in range(nlen):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, nlen):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                c = - nums[i] - nums[j]
                if nums[i] <= c and nums[j] <= c and self.__binarySearch(nums, j + 1, nlen - 1, c) != -1:
                    ans.append([nums[i], nums[j], c])
        return ans


s = Solution()
while True:
    nums = eval(input())
    print(s.threeSum(nums))
