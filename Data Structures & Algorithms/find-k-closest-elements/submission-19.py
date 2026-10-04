class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dict1 = {}
        abc = []
        for i in range(len(arr)):
            diff = abs(arr[i] - x)
            dict1[(diff, i)] =  arr[i]
        # print(dict1) 

        # print(sorted(dict1.keys())[:k])
        l = sorted(dict1.keys())[:k]

        for i in l:
            if i in dict1:
                abc.append(dict1[i])
        

        # for ke,v in dict1.items():
        #     if ke in l: 
        #         abc.append[dict1[ke]]
                    
        # print(abc)
        return sorted(abc)




        

            
            
        
         
