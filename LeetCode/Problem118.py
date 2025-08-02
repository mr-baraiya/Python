class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1]
            if ( i > 0):
                prevRow = triangle[i-1]
                for j in range(1,i):
                    row.append(prevRow[j-1] + prevRow[j])
                row.append(1)
            triangle.append(row)
        return triangle
