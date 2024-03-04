class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum = 0
        prev = 0
        for char in s:
            val = dict_roman[char]
            sum+= val
            if val>prev:
                sum-= 2*prev
            prev = val
        return sum
