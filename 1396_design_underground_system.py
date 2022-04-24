class UndergroundSystem:

    def __init__(self):
      self.graph=[]
      self.time=[]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
      self.graph.append([id, stationName, t])
    
    def find(self,id):
      for item in self.graph:
        if item[0]==id:
          self.graph.remove(item)
          return item
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        initial=self.find(id)
        self.time.append([initial[1], stationName, (t-initial[2])])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
      count=0
      sum=0
      for item in self.time:
        if item[0]==startStation and item[1]==endStation:
          count +=1
          sum +=item[2]
      if count ==0:
         return 0
      return (sum/count)