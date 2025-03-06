class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        output_arr = []
        freq = {}
        hash_dict = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] not in hash_dict:
                    hash_dict[grid[i][j]] = 1
                else:
                    output_arr.append(grid[i][j])
        nums = hash_dict.keys()
        for k in range(1,n*n+1):
            if k not in nums:
                output_arr.append(k)
        return output_arr
        # for row in grid:
        #     for col in row:
        #         freq[col] = freq.get(col,0)+1

        # for num in range(1,n*n+1):
        #     if num not in freq:
        #         missing = num
        #     elif freq[num]==2:
        #         repeat = num
        # return [repeat,missing]