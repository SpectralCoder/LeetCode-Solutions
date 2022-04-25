class PeekingIterator:
    def __init__(self, iterator):
      self.iterator=iterator
      self.nextval = self.iterator.next()

    def peek(self):
      return self.nextval
        

    def next(self):
      item =self.nextval
      running = self.iterator.next()
      if running >0:
        self.nextval=running
      else:
        self.nextval = None
      return item
        

    def hasNext(self):
      return self.nextval != None