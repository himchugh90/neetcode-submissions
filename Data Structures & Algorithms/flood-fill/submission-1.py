class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color  = image[sr][sc] 
        if original_color== color:
            return image
            
        def dfs(r,c,image,original_color):    
            image[r][c] = color
            dirs = [(0,1), (0,-1), (-1,0), (1,0)]
            for d in dirs:
                new_r, new_c = r+d[0], c+d[1]
                if inbounds(new_r, new_c, image) and image[new_r][new_c] == original_color:
                    dfs(new_r,new_c,image,original_color)

        def inbounds(r,c,image):
            return 0<=r<len(image) and 0<=c<len(image[0])
        
        # for i in range(len(image)):
        #     for j in range(len(image[0])):
        #         if i == sr and j == sc:
        dfs(sr,sc,image,original_color)                    
        return image