
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        k %= n
        
        for i in range(m):
            if i % 2 == 0:
                s = mat[i][k:] + mat[i][:k]     
            else:
                s = mat[i][-k:] + mat[i][:-k]
            
            if s != mat[i]:
                return False
        
        return True