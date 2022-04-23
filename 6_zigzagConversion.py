class Solution:
    def convert(self, s: str, numRows: int) -> str:
      datalist=[]
      for i in range(numRows):
        datalist.append([])
      index = (numRows+(numRows-1))-1
      if index == 0:
        return s
      elif index < 0:
        return ''
      for i in range(len(s)):
        if i%index == 0:
          datalist[i%index].append(s[i])
        elif i%index == numRows-1:
            datalist[i%index].append(s[i])
        elif int(i/(numRows-1))%2==0:
          datalist[i%(numRows-1)].append(s[i])
        elif int(i/(numRows-1))%2==1:
          datalist[(numRows-1)-(i%(numRows-1))].append(s[i])

      actual_str=''
      for item in datalist:
          strh=''.join(str(v) for v in item)
          actual_str += strh
      return actual_str