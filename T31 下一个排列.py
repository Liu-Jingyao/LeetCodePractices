from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        end_index = len(nums) - 1
        start_of_no_increase = end_index

        while start_of_no_increase > 0:
            if nums[start_of_no_increase] > nums[start_of_no_increase - 1]:
                break
            start_of_no_increase -= 1

        if start_of_no_increase == 0:
            nums.reverse()
            return

        need_be_swapped = start_of_no_increase - 1
        for i in range(end_index, start_of_no_increase - 1, -1):
            if nums[i] > nums[need_be_swapped]:
                nums[i], nums[need_be_swapped] = nums[need_be_swapped], nums[i]
                break

        while start_of_no_increase <= end_index:
            nums[start_of_no_increase], nums[end_index] = nums[end_index], nums[start_of_no_increase]
            start_of_no_increase += 1
            end_index -= 1


s = Solution()
while True:
    nums = eval(input())
    s.nextPermutation(nums)
    print(nums)
