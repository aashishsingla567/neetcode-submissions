class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # pretend its linear
        n = len(matrix)
        m = len(matrix[0])
        print('nm', n, m)
        size = n * m
        def get_i(x):
            i = x // m
            j = x % m
            # print(x, "->", (i, j), "=",matrix[i][j])
            return matrix[i][j]
        
        l, r = 0, size - 1
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, mid)
            val = get_i(mid)
            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False