class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
   
        dict1={}
        for id, num in enumerate(nums):
            dict1[id] = num
        print(dict1)
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i !=j and dict1[i] == dict1[j] and abs(i-j) <=k:
                    return True
        return False


        # l = 0
        # n = len(nums) 
        # r = n - 1

        # while l < r and r<=n-1:
        #     if (nums[l] != nums[r] and abs(l-r) >=k) :
        #         print(l,r)
        #         r-=1
        #         # return False
        #         # break
        #     elif (nums[l] == nums[r] and abs(l-r) <=k) :
        #         # print(l,r)
        #         return True  
        #     l+=1
        # return False
        