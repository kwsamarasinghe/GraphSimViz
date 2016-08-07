import httplib
import sys

#REST client which performs a HTTP request to the GraphML server
class RestClient:

    def __init__(self,url):
        self.url=url
        try:
            self.connection=httplib.HTTPConnection(url)
        except HTTPException as error:
            raise Exception("Error connecting "+ url)

    #performs a HTTP GET request
    def get(self,resource,parameters):
        try:
            self.connection.request("GET",resource)
            r=self.connection.getresponse()
            return r.read()
        except Exception as error:
            raise Exception("Error requesting resouce "+ resource)
