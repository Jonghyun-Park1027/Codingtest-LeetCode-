class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            left = i
            right = len(nums) -1    
            while left < right:
                num = nums[left] + nums[right]
                if num == target :
                    return [left, right]
                # left += 1
                right -= 1
            