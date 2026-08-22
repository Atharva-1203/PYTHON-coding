class Solution(object):
    def spiralOrder(self, matrix):
        ans=[]
        m=len(matrix)
        n=len(matrix[0])
        rowstart=0
        colstart=0
        rowend=m-1
        colend=n-1

        c=0
        total=m*n
        while c<total:
            #Print rowstart elements from colstart to colend
            for i in range(colstart,colend+1):
                ans.append(matrix[rowstart][i])
                c+=1
            rowstart+=1

            #Print colend elements from rowstart to rowend
            for j in range(rowstart,rowend+1):
                ans.append(matrix[j][colend])
                c+=1
            colend=colend-1

            #Print rowend elements from colend to colstart
            if rowstart <= rowend:
                for k in range(colend, colstart - 1, -1):
                    ans.append(matrix[rowend][k])
                    c += 1
                rowend -= 1

            if colstart <= colend:
                for l in range(rowend, rowstart - 1, -1):
                    ans.append(matrix[l][colstart])
                    c += 1
                colstart += 1

        return ans 

                

        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        