class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)
        b = len(word2)
        l = 0
        r = 0
        s=""
        if a>b:
            s1 = word1[b:]
        else:
            s1 = word2[a:]
        abc = []

        for l in range(min(a,b)):
            s = word1[l] + word2[l]  
            abc.append(s)
        abc.append(s1)
        # print(abc)
        s2 = "".join(str(x) for x in abc)
        return s2
        
            