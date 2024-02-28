class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                neighbors_sum = 0
                count = 0
                for ni in range(max(0, i - 1), min(m, i + 2)):
                    for nj in range(max(0, j - 1), min(n, j + 2)):
                        neighbors_sum += img[ni][nj]
                        count += 1
                result[i][j] = neighbors_sum // count
        
        return result
