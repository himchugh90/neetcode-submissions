class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(word2[2:])
        # print(word1[2]+word2[0])
        a = len(word1)
        b = len(word2)
        c= ""
        abc = []
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i==j:
                    c = word1[i] + word2[j]
                    abc.append(c)
                    break
        if a<b:
            abc.append(word2[a:])
        else:
            abc.append(word1[b:])

        for i in range(len(abc)):
            a = "".join(str(x) for x in abc)
        return a
                
                
            




        
        # print(word1+word2)
        # word3 = word1+word2
        # a = len(word1)
        # b = len(word2)
        # l = 0
        # # r = len(word1)
        # abc = []
        # c = ''
        # while l <= min(a,b):
        #     c += word1[l] + word2[l]
        #     if b > a:
        #         c= c+ word2[l:]
        #     elif a > b:
        #         c = c+word1[l:]


        # print(c)


            


        