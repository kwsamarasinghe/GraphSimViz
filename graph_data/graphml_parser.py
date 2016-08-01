from graph_tool import Graph
from xml.dom import minidom

#Parser for GraphML which parses a graphml document/string into a
#graphtool Graph
class GraphMLParser:

    #parses a string into a graph_tool Graph object
    #This is a very minimal parser which barely constrcuts the nodes and edges
    def parse_graph_from_string(self, graphML_string):
        dom = minidom.parseString(graphML_string)
        root = dom.getElementsByTagName("graphml")[0]
        graph = root.getElementsByTagName("graph")[0]
        name = graph.getAttribute('id')

        g = Graph(directed=False)

        vpos=g.new_vertex_property("vector<double>")
        for node in graph.getElementsByTagName("node"):
            id=node.getAttribute('id')
            n = g.add_vertex()
            g.vertex_index[id]

            #right now only the positions are available
            for attr in node.getElementsByTagName("data"):
                if attr.firstChild:
                    key=attr.getAttribute("key")
                    #n[key] = attr.firstChild.data
                    if(key=="x"):
                        x=attr.firstChild.data
                    elif(key=="y"):
                        y=attr.firstChild.data

            vpos[id]=(x,y)

        g.vertex_properties["pos"]=vpos

        #have to workaround the directed graph written by the server
        for edge in graph.getElementsByTagName("edge"):
            source = edge.getAttribute('source')
            dest = edge.getAttribute('target')
            e = g.add_edge(source, dest)

	return g
