class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False]*(len(s)+1)   # example 1       [FALSE],[FALSE],[FALSE],[FALSE],[FALSE],[FALSE],[FALSE][FALSE][FALSE]
        dp[0] = True              # 빈 문자열이 되면 성공
        # for word in wordDict:
        #     for i in range(len(s)+1): # example 1   for i in range(9)
        #             if s[i:len(word)] == word:
        for i in range(len(s) + 1):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i + len(word)] = True

        return dp[len(s)]


      

        