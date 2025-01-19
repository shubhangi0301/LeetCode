class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr = []
        if(m*n)!=len(original):
            return arr
        else:
            counter = 0
            for i in range(m):
                if counter < len(original):
                    arr.append(original[counter : counter + n])
                    counter += n
            return arr
                # original = original[]
                # for j in range(n):
                #     original = original[j:]
                #     arr[i][j] = original[0]

        