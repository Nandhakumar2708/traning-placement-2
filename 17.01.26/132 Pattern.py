class Solution:
    def find132pattern(self, a):
        st=[]; s3=-10**18
        for x in a[::-1]:
            if x<s3: return True
            while st and st[-1]<x:
                s3=st.pop()
            st.append(x)
        return False
