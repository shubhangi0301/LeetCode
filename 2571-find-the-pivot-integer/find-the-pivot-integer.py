class Solution(object):
    def sums(self,n):
        return (n*(n+1))//2
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        else:
            i = n-1
            j = n
            while(self.sums(i)>=(self.sums(j)-self.sums(i-1))):
                if(self.sums(i)==(self.sums(j)-self.sums(i-1))):
                    return i
                else:
                    i-= 1
        return -1