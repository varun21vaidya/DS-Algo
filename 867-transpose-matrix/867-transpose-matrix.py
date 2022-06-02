class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        mat=[[]for i in range(n)]
        print(mat)
        for i in range(m):
            for j in range(n):
                mat[j].append(matrix[i][j])



        return mat
    
                   
            
            
        
            