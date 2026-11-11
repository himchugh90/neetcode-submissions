class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                p+=prices[i] - prices[i-1]
        return p
        # l = 0
        # r = 1
        # n = len(prices)
        # p = 0

        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         if prices[j] > prices[i]:
        #             pass

        #     return prices[-1] - prices[0]

        # while l<r and r<= n-1:
        #     if prices[l] < prices[r]:
        #         l+=1
        #         r+=1
        #     else:
        #         break
        #     return 
        # while l<r and r <= n-1:
        #     diff = 0
        #     if prices[l] < prices[r]:
        #         diff = prices[r] - prices[l]
        #         p+=diff
        #         l = r+1
        #         r=r+2

        #     else:
        #         l+=1
        #         r+=1
        # return p


                

        



        