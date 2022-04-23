from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
      start=0
      end=len(nums)-1
      if(nums[start] == target):
        return start
      elif (nums[end] == target):
        return end
      while start != end and start != (end-1):
        center= int((start+end)/2)
        print(start)
        print(end)
        print(center)
        if nums[center]== target:
          return center;
        elif nums[center]>target:
          end=center
        else:
          start=center
      return -1