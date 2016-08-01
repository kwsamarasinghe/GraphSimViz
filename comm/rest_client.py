import httplib

#REST client which performs a HTTP request to the GraphML server
class RestClient:

    #url and port of the graphml server
    url=""

    #connection
    connection=None

    def __init__(self,url):
        self.url=url
        self.connection=httplib.HTTPConnection(url)

    #performs a HTTP GET request
    def get(self,resource,parameters):
        self.connection.request("GET",resource)
        try:
            r=self.connection.getresponse()
            return r.read()
        except Exception as e:
            print "error performing GET "+e
