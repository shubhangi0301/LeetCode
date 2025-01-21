import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        out = []
        result = 0
        for x in num:
            result = result * 10 + x
        res = result+k
        # out = [int(x) for x in str(res)]
        for p in str(res):
            out.append(int(p))
        return out