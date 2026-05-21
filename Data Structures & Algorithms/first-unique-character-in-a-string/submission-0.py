class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = [x for x in str(s)]
        # print(a)
        dict1 = Counter(a)
        # print(dict1)
        # for k,v in dict1.items():
        for i in range(len(a)):
            if dict1[a[i]] == 1:
                return i
        return -1
        