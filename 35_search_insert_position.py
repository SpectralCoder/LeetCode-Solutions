class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      start=0
      end=len(nums)-1
      if nums[start] == target or target<nums[start]:
        return start
      elif  nums[end] == target  :
        return end
      elif nums[end]<target:
        return end+1
      while start<=end:
        center = start + (end - start)//2
        if nums[center]== target:
          return center
        elif target<nums[center] and target>nums[center-1]:
          return center
        elif nums[center]>target:
          end=center-1
        else:
          start=center+1
      return -1