class Solution:
    def coloredCells(self, n: int) -> int:
        i = 0
        for x in range(1,n+1):
            sum = (x**2)+(x-1)**2
            i = sum
        return sum
        