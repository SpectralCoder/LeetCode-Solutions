class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        val=(len(nums1)+len(nums2))/2
        prev=0
        m=0
        n=0
        for i in range(int(val)+1):
          if m<len(nums1) and n<len(nums2):
            if i == int(val):
              if val%1 != 0:
                if nums1[m]>nums2[n]:
                  return(nums2[n])
                else:
                  return(nums1[m])
              else:
                if nums1[m]>nums2[n]:
                  return((nums2[n]+prev)/2)
                else:
                  return((nums1[m]+prev)/2)
            elif nums1[m]>nums2[n]:
              prev=nums2[n]
              n=n+1

            else:
              prev=nums1[m]
              m=m+1
          elif m<len(nums1):
            if i == int(val):
              if val%1 != 0:
                return(nums1[m])
              else:
                return((nums1[m]+prev)/2)
            else:
              prev=nums1[m]
              m=m+1 
          else:
            if i == int(val):
              if val%1 != 0:
                return(nums2[n])
              else:
                return((nums2[n]+prev)/2)
            else:
              prev=nums2[n]
              n=n+1 