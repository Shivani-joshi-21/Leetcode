class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        
        ans =nums1 + nums2
        ans.sort()
        n= len(ans)
        if n % 2 == 0:
            median1 = ans[n//2]
            median2 = ans[n//2 - 1]
            median = (median1 + median2)/2
        else:
            median = ans[n//2]
        
        return median
