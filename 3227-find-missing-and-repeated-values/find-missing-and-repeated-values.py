class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        output_arr = []
        hash_dict = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in hash_dict:
                    hash_dict[grid[i][j]] = 1
                else:
                    output_arr.append(grid[i][j])
        nums = hash_dict.keys()
        for k in range(1,n**2+1):
            if k not in nums:
                output_arr.append(k)
        return output_arr