class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
      squared = [x**2 for x in nums]
      result= self.mergeSort(squared)
      return result

    def mergeSort(self, nums: List[int]) -> List[int]:
      if len(nums) >1:
        center= len(nums)//2
        left=nums[:center]
        right=nums[center:]
        left = self.mergeSort(left) #left half
        right= self.mergeSort(right) #right half
        i=j=k=0
        while i<len(left) and j<len(right):
          if left[i]<right[j]:
            nums[k]=left[i]
            i +=1
          else:
            nums[k]=right[j]
            j +=1
          k +=1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return nums
      return nums