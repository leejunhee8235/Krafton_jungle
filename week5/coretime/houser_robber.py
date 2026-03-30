# 198. House Robber
# 도둑질

# 당신은 길거리에 있는 집들을 털 계획을 세우고 있는 전문 도둑이다.
# 각 집에는 일정 금액의 돈이 숨겨져 있다.

# 그런데 한 가지 제약이 있다.
# 서로 인접한 두 집을 같은 밤에 털면, 그 집들의 보안 시스템이 연결되어 있어서 자동으로 경찰에 신고된다.

# 정수 배열 nums가 주어질 때,
# nums[i]는 i번째 집에 있는 돈의 양을 의미한다.

# 경찰에 걸리지 않으면서 오늘 밤 훔칠 수 있는 최대 금액을 반환하라.




# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = 0
#         dp = [0]*len(nums)

#         for i in range(len(nums)): # 0 1 2 3 
#             dp[i] = nums[i]+nums[i-2]+nums[i+2]   
#             # dp[0] = nums[0] + nums[-2] + nums[2], dp[1] = nums[1]+nums[-1]+nums[3], 
#             # dp[2] = nums[2]+nums[0]+nums[4] , dp[3] = nums[3]+nums[1]+nums[5]

        
#         return max(dp)


class Solution(object):
    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
    



     