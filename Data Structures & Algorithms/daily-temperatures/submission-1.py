class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dict1 = {}
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                # print(i,j)
                if temperatures[i] < temperatures[j]:
                    dict1[i] = j-i
                    break
                else:
                    dict1[i] = 0
        # print(dict1.values())
        return list(dict1.values())

        































        # n = len(temperatures)
        # res = [0]*n
        # print(res)
        # stack =[]
        # dict1={}
        # for id, t in enumerate(temperatures):
        #     dict1[t]=id
        
        # l=0
        # r=1
        # for i in range(len(temperatures)):
        #     while l<r and r<= len(temperatures)-1:
        #         stack.append(l)
        #         if temperatures[l] < temperatures[r]:
        #             res[i]  = r-l
        #             stack.pop()
        #         else:
        #             r+=1
        #         l+=1
        #         # r+=1
        # return res
        




        






















            

            
            


        # for i in range(len(temperatures)):
        #     stack.append(temperatures[i])
        #     if 










        # for i in range(1,len(temperatures)):
        #     # stack.append(temperatures[i])
        #     if temperatures[i] > stack[-1]:
        #         dict1[stack[-1]] = i
        #         stack.pop()
                
        #     stack.append(temperatures[i])
        # print(dict1)
                




        # dict1={}
        # for i in range(len(temperatures)):
        #     for j in range(len(temperatures)):
        #         if i < j and temperatures[i] < temperatures[j]:
        #             # print(i,j)
        #             dict1[i] = j-i
        #             break
        #         else:
        #             dict1[i] = 0
        # # print(dict1)
        # return [x for x in dict1.values()]
            




        # # dict1={}
        # dict2 = {}
        # # for id, num in enumerate(temperatures):
        # #     dict1[num] = id 
        # l = 0
        # r = 1
        # while l<r :
        #     r = l+1
        #     while r<= len(temperatures) -1:
        #         if temperatures[l] < temperatures[r]:
        #             dict2[l] = r-l
        #             break
        #         l+=1
                    
        #         #     r+=1

        #         # else:
        #         #     dict2[l] = r-l
        #         #     l+=1
        #         #     break
            
        # return dict2    








        # stack = []
        # abc = [] #[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     if stack:
        #         if stack[-1] < temperatures[i]:
        #             print(stack[-1])
        #             stack.pop()
        #             abc.append(i)
        #             continue
        #         else:
        #             print(stack[-1])
        #             stack.pop()
        #             abc.append(0)
            
        #     # if stack==[]:
        #     stack.append(temperatures[i])    
        # return abc    