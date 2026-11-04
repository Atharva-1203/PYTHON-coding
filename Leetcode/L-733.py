class Solution(object):
    def floodFill(self, image, sr, sc, color):

        m = len(image)
        n = len(image[0])

        org = image[sr][sc]

        if org == color:
            return image

        def dfs(row, col):

            image[row][col] = color

            if row > 0 and image[row-1][col] == org:
                dfs(row-1, col)

            if row < m-1 and image[row+1][col] == org:
                dfs(row+1, col)

            if col > 0 and image[row][col-1] == org:
                dfs(row, col-1)

            if col < n-1 and image[row][col+1] == org:
                dfs(row, col+1)

        dfs(sr, sc)

        return image
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        