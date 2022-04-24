class Solution:
   def firstBadVersion(self, n: int) -> int:
        checkAfter=False
        checkBefore= True
        start=0
        end=n
        while start < end:
            center= int((start+end)/2)
            check= isBadVersion(center)
            if center<=end-1:
                checkAfter= isBadVersion(center+1)
            if center>0:
                checkBefore= isBadVersion(center-1)

            print(check)
            if check == False and checkAfter == True :
                return center+1
            elif check == True and checkBefore == False:
                return center
            elif check == False:
                start=center
            else:
                end=center
        return -1