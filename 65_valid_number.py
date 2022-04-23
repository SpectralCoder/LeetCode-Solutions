class Solution:
    def isNumber(self, s: str) -> bool:
      muldeci=0
      mulexpo=0
      valid=0
      signvalid=0
      imi=0
      spec=0
      if s[0] == 'e' or s[0] == 'E':
        return False
      elif s[0] == '.':
        if len(s)<=1:
          return False
      for i in s:
        if muldeci>=2 or mulexpo >=2:
          return False
        elif i.isdigit():
          signvalid=1
          valid=0
          imi=0
          spec=1
        elif i== '.' and valid ==0:
          signvalid=1
          muldeci=muldeci+1
          if imi==1:
            return False
          else:
            imi=imi+1
        elif (i == 'e' or i=='E') and valid==0 and spec==1:
          signvalid=0
          mulexpo=mulexpo+1
          valid=1
          imi=imi+1
          if muldeci !=1:
            muldeci=muldeci+1

        elif (i== '+' or i== '-') and signvalid==0 :
          signvalid=1
        else:
          return False

      if(valid !=0  or muldeci>=2 or mulexpo >=2 or spec==0):
        return False
      else:
        return True
