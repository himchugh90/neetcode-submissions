import numpy as np
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # print(nums[:0])
        res = [0]*len(nums)
        n = len(nums)
    
        for i in range(n):
            left_p = nums[:i]
            right_p = nums[i+1:]
            f_p = left_p + right_p
            p = math.prod(f_p)
            res[i] = p
        return res
        # l = 0
        
        # res = [0]*len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         p=1
        #         p=p*nums[j]

        #     res[i] = 

















        # prod = 1
        # res = [0]*len(nums)
        # # print(res)
        # for i in range(len(nums)):
        #     prod = prod*nums[i]
        # for i in range(len(nums)):
        #     try :
        #         res[i] = prod/nums[i]
        #     except:
        #         res[i] = 0
        # print(prod)
        # print(res)

        
        


      

















