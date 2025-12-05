class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cnt = sum(nums[:k])
        maximum = cnt

        left=0
        right = left + k - 1
        end = len(nums) - 1
        while right < end :

            
            right += 1
            cnt = cnt - nums[left] + nums[right]

            maximum = max(maximum, cnt)

            left += 1
            
        
        return maximum/k