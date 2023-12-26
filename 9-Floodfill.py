class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        startImage = image[sr][sc]

        self.dfs(image, sr, sc, color, startImage)

        return image
    

    def dfs(self, image, sr, sc, color, startImage):

        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0])-1 or image[sr][sc] == color or image[sr][sc] != startImage:
            return
        
        image[sr][sc] = color
        self.dfs(image, sr+1, sc, color, startImage)
        self.dfs(image, sr-1, sc, color, startImage)
        self.dfs(image, sr, sc+1, color, startImage)
        self.dfs(image, sr, sc-1, color, startImage)


solution_instance = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
result = solution_instance.floodFill(image, sr, sc, color)
print(result)