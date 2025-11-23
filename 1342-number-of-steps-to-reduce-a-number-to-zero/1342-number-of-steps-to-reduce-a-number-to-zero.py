class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        steps = 0
        while num:
            if num & 1:  # 맨 끝 비트가 1이면 (홀수)
                steps += 2
            else:        # 맨 끝 비트가 0이면 (짝수)
                steps += 1
            num >>= 1    # 오른쪽으로 1비트 시프트 (÷2 효과)
        return steps - 1  # MSB의 과잉 계산 보정