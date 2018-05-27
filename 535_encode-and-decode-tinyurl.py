# -*- coding:utf-8 -*-

class Codec:
    def __init__(self):
        self.url2code = {}
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shortUrl = 'http://tinyurl.com/'+ str(hash(longUrl))
        self.url2code[str(hash(longUrl))] = longUrl
        return shortUrl
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = str.split(shortUrl, '/')[-1]
        longUrl = self.url2code[key]
        return longUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
