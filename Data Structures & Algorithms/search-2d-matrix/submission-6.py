class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # pretend its linear
        n = len(matrix)
        m = len(matrix[0])
        size = n * m
        l, r = 0, size - 1
        while l <= r:
            mid = (l + r) // 2
            i = mid // m
            j = mid % m
            # print(l, r, mid)
            val = matrix[i][j]
            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False