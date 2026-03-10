class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        
        if n < 0:
            return 1 / (x ** (-n))
        
        return x ** n


    # for i in range(n+1): # 1 2 3 
            
    #         x ** i
    #         if n < 0:
    #             minus = 1/n
    #             return x
    #         return x


    # class Solution(object):
    #     def myPow(self, x, n):

    #         if n == 0:
    #             return 1
            
    #         if n < 0:
    #             x = 1 / x
    #             n = -n
            
    #         result = 1
            
    #         while n > 0:
    #             if n % 2 == 1:
    #                 result *= x
                
    #             x *= x
    #             n //= 2
            
    #         return result