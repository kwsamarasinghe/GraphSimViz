from comm.rest_client import RestClient
from graph_data.graphml_parser import GraphMLParser
from threading import Timer

#Graph data handler class
#This class is responsible of handling the graph data querying a server
#It initializes a graph with the data from the server
#Also updates a graph continuously polling the server
class GraphDataHandler:

    rest=None
    parser=None

    def __init__(self,url):
        self.rest=RestClient(url)
        update_timer=Timer(10,self.update_graph)
        update_timer.start()

    #initializes the graph from the graph data queried from the server
    def init_graph(self):
        #performs a request
        graphml=self.rest.get("/graph/graph","")

        #Initializes the graph parsing the graphml from the server
        parser=GraphMLParser()
        g=parser.parse_graph_from_string(graphml)
        return g

    #callback function on the graph updates
    def update_graph(self):
        #Sets up a callback to notify the updates
        print "calling updates"
