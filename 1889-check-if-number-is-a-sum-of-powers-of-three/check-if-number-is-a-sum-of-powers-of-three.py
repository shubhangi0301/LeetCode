class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # while n>0:
        #     p = 0
        #     while(3**p<=n):
        #         p+= 1
        #     # num = 3**p
        #     while(p>0):
        #         if(n-3**p>=1):
        #             n-= 3**p
        #             p-= 1
        #         else:
        #             # return false
        #             break
        # return False
        p = 0
        while(3**p<=n):
            p+= 1
        while(n>0):
            if(n>=3**p):
                n-= 3**p
            if(n>3**p):
                return False
            p-= 1
        return True

