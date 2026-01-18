class Solution:
    def fourSumCount(self, A, B, C, D):
        from collections import Counter
        ab=Counter(a+b for a in A for b in B)
        return sum(ab[-c-d] for c in C for d in D)
