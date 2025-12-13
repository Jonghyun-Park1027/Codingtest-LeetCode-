class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        n = len(nums)
        ans = 0
        for i in range(1,n):
            prefix.append(prefix[i-1] + nums[i])
        print(prefix)
        for j in range(n-1):
            if prefix[j] >= prefix[n-1] - prefix[j] :

                ans += 1
        return ans 