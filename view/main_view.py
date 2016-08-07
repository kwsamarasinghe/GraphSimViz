from graph_tool.all import *
from numpy.random import *
from graph_data.graph_data_handler import GraphDataHandler

import sys, os, os.path
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject

#graph window
data_handler=GraphDataHandler("localhost:8111")
if(data_handler!=None):
    g=data_handler.init_graph()

    if(g!=None):
        pos = g.vertex_properties["pos"]
        win = GraphWindow(g, pos, geometry=(500, 400))
        win.connect("delete_event", Gtk.main_quit)
        win.show_all()
        Gtk.main()
    else:
        print "Unable to load the graph, quitting"
else:
    print "Unable to connect to graph server"
