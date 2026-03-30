class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 베이스케이스
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # dp 배열생성 및 초기화
        dp = [0]*(n+1)
        # dp 주소에 값을대입
        dp[1] = 1
        dp[2] = 2

        # 반복문을 돌리며 상향하는 식
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
        
        #점화식 dp[i] = dp[i-1]+dp[i-2]