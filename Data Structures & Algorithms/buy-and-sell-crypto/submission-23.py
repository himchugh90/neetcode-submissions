class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        # p = 0
        max_p = 0
        while l<len(prices) : 
            r = l+1
            while r< len(prices):
                # if prices[r] > prices[l]:
                print(l,r)
                p = prices[r] - prices[l]
                if p>0:
                    max_p = max(max_p, p)
                    # r+=1
                else:
                    pass
                
                r+=1
            l+=1
        return max_p

        

       
            























        # l = 0
        # r = 1
        # max_p = 0
        # while l<r and r<=len(prices)-1:
        #     print(l,r)
        #     if prices[l] < prices[r]:
        #         p = prices[r] - prices[l]
        #         max_p = max(p, max_p)
        #     else:
        #         l=r
        #     r+=1
            
        # return max_p
            
            























        # min_price = float('inf')
        # best = 0
        # for p in prices:
        #     if p < min_price:
        #         min_price = p
        #     # else:
        #     best = max(best, p - min_price)
        #     print(best)
        # return best
        # left_pt = 0
        # right_pt = 1
        # min_price = 0
        # max_profit = 0
        # while left_pt < right_pt and right_pt <= len(prices) - 1:
            
        #     if prices[left_pt] > prices[right_pt]:
        #         if len(prices) == 2:
        #             return 0
        #         else:
        #             left_pt +=1
        #             right_pt+=1
        #     if prices[left_pt] < prices[right_pt]:
        #         print(prices[left_pt])
        #         print(prices[right_pt])
        #         min_price = prices[left_pt]
        #         profit = prices[right_pt] - prices[left_pt]
        #         print(max_profit)
        #         if profit> max_profit:
        #             max_profit = profit
                    
        #     right_pt+=1
            
        # return max_profit
        
        