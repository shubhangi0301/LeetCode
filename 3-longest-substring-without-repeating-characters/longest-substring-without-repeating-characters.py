class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
        if len(s)>1:
            maxlen = 0
            for i in range(len(s)):
                count=0
                str_dict = {}
                for j in range(i,len(s)):
                    if s[j] not in str_dict:
                        count+=1
                        # maxlen = max(maxlen,j-i+1)
                        str_dict[s[j]] = count
                    else:
                        break
                maxlen=max(maxlen,count)
            return maxlen
