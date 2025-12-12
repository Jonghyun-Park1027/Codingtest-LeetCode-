class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # print(nums.split(0))
        k_cp = k
        cnt = 0
        maximum = 0
        for i in range(len(nums)):
            if nums[i]:
                cnt += 1
                continue
            else :
                k -=1
                cnt += 1
            if not k :
                k = k_cp
                maximum = max(maximum, cnt)
                cnt = 0
                continue
            
        return maximum