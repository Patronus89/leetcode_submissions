from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target:int)-> List[int]:
        """
        Find two numbers that add up to target.
        Returns indices of the two numbers.
        """
        print(range(len(nums)))
        for i in range(len(nums)):
             for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]                


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 3]
    target = 6
    print(solution.twoSum(nums, target))