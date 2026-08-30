class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        n = len(piles)
        l, r = 1,max(piles)
        # abc = []
        # t=0
        res = r
        while l<=r :
            m = (l+r)//2
            t=0
            for i in range(len(piles)):
                s = math.ceil(piles[i]/m)
                t = t+ s
        
            if t<=h:
                res = m
                # return m
                # abc.append(m)
                r = m-1
            
            else:# t> h:
                l = m+1
        return res
        



        