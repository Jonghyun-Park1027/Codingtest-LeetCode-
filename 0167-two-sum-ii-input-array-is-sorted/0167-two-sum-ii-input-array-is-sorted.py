class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # print(numbers)
        answer = {}
        for i, v in enumerate(numbers):
            if target-v not in answer :
                answer[v] = i
            else :
                return [answer[target-v]+1, i+1 ]
