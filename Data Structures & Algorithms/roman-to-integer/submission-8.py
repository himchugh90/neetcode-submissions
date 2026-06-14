class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        val = 0
        n = len(s)
        l = 0
        r = 1
        
        while l<=n and r<=n:
           
            if s[l:r+1] == 'IX' :
                val += 9
                l+=2
                r+=2
                # print(val)
            elif s[l:r+1] == 'IV' :
                val += 4
                l+=2
                r+=2
                # print(val)
            elif s[l:r+1] == 'XL' :
                val += 40
                l+=2
                r+=2
                # print(val)
            elif s[l:r+1] == 'XC' :
                val += 90
                l+=2
                r+=2
                # print(val)
            elif s[l:r+1] == 'CD':
                val += 400
                l+=2
                r+=2
                # print(val)
            elif s[l:r+1] == 'CM':
                val += 900
                l+=2
                r+=2
                # print(val)
            else:
                val+=dict1[s[l:r]]
                # print(l, r, val)
                l+=1
                r+=1
          
        return val

        
        



        