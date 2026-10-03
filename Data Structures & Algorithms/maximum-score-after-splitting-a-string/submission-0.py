class Solution:
    def maxScore(self, s: str) -> int:
        # cnt = 0
        # l = 0
        # n = len(s)
        # while l < n:
        #     left = s[:l]
        #     right = s[l:]
        s1 = list(s)
        max_cnt = 0
        for i in range(1,len(s1)):
            l = s1[:i]
            r = s1[i:]
            # print(l, r)
            max_cnt = max(max_cnt, l.count('0') + r.count('1'))
            # print(max_cnt)
        return max_cnt


        