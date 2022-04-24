class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      k=k%len(nums)
      cutpoint= len(nums)-k
      temp=nums[:cutpoint]
      del nums[:cutpoint]
      nums +=temp