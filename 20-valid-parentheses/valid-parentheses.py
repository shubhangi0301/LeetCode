class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        bracket_mapping={'(':')','{':'}','[':']'}
        for char in s:
            if char in bracket_mapping.keys():
                stack.append(char)
            elif char in bracket_mapping.values():
                if not stack:
                    return False
                elif bracket_mapping[stack.pop()]!=char:
                    return False
        return len(stack)==0
