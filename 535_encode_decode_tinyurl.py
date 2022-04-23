from random import choice 
class Codec:
    
    def __init__(self):
        self.charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.urls = {}
        
    def get_key(self):
        return ''.join(choice(self.charset) for i in range(6))
            
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        response= self.checkDuplicate(longUrl)
        if response != False:
          return response
        key = self.get_key() 
        while key in self.urls: # generate a non-existing key
            key = self.get_key()
        
        self.urls[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl[shortUrl.rindex('/')+1:]
        return self.urls[key] if key in self.urls else ''
    def print(self):
      print(self.urls)

    def checkDuplicate(self, url: str) -> str:
      if url in self.urls.values():
        for key, value in self.urls.items():
          if value == url:
            return "http://tinyurl.com/" + key
      else:
        return False