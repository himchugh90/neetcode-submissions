class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]
        # print(symList[0][0],symList[0][1]) 
        
        res = ""
        symList.reverse() 
        for i in range(len(symList)):
            # while num:
            div = num//symList[i][1]  
            # print(div)
            if div >= 1:
                res+= symList[i][0]*div
                num = num%symList[i][1] 
                # print(num)
            else:
                pass 
        return res