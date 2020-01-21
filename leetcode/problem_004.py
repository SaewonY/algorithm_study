'''
Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        collected = []
        
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] >= nums2[j]:
                collected.append(nums2[j])
                j += 1
            else:
                collected.append(nums1[i])
                i += 1
                
        while i < len(nums1):
            collected.append(nums1[i])
            i += 1
        while j < len(nums2):
            collected.append(nums2[j])
            j += 1
        
        if len(collected) % 2 != 0:
            mid = len(collected) // 2
            median = collected[mid]
        else:
            mid= len(collected) // 2
            median = (collected[mid-1] + collected[mid]) / 2
            
        return median