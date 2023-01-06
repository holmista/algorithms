class Solution:
    def searchMatrix(self, matrix, target):
        l = 0
        r = len(matrix)-1
        rowIdx = 0
        while l < r:
            m = (l+r) // 2
            if matrix[m][0] == target:
                rowIdx = m
                break
            if matrix[m][0] < target:
                if abs(r-m) <= 1:
                    if matrix[m][-1] >= target:
                        rowIdx = m
                    else:
                        rowIdx = r
                    break
                l = m
            elif matrix[m][0] > target:
                if abs(l-m) <= 1:
                    rowIdx = l
                    break
                if r==m and matrix[m][0]>target:
                    return False
                r = m
        l = 0
        r = len(matrix[0]) - 1 
        while l <= r:
            m = (l + r) // 2
            if matrix[rowIdx][m] == target:
                return True
            if matrix[rowIdx][m] > target:
                r = m
            else:
                l = m+1
            if l==r and matrix[rowIdx][l] != target:
                    return False
        return False

sol = Solution()
answer = sol.searchMatrix([[-10,-10],[-9,-9],[-8,-6],[-4,-2],[0,1],[3,3],[5,5],[6,8]], 0)
print(answer)