class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s=='':
            return 0
        biggest_string={}
        for k,v in enumerate(s):
            append_str=v
            for key,val in enumerate(s[k+1:]):
                if val not in append_str:
                    append_str=append_str+val
                else:
                    biggest_string[len(append_str)]=append_str
                    break
            else:
                biggest_string[len(append_str)]=append_str

        if len(biggest_string)!=0:
            return max(biggest_string.keys())
        else:
            return 1
