from graph_tool.all import *
from numpy.random import *
from graph_data.graph_data_handler import GraphDataHandler

import sys, os, os.path
from gi.repository import Gtk, Gdk, GdkPixbuf, GObject

#graph window
data_handler=GraphDataHandler("localhost:8111")
g=data_handler.init_graph()
pos = g.vertex_properties["pos"]
win = GraphWindow(g, pos, geometry=(500, 400))

# This function will be called repeatedly by the GTK+ main loop, and we use it
# to update the state according to the SIRS dynamics.
def update_state():
    newly_infected.a = False
    removed.a = False

    # visit the nodes in random order
    vs = list(g.vertices())
    shuffle(vs)
    for v in vs:
        if state[v] == I:
            if random() < r:
                state[v] = R
        elif state[v] == S:
            if random() < x:
                state[v] = I
            else:
                ns = list(v.out_neighbours())
                if len(ns) > 0:
                    w = ns[randint(0, len(ns))]  # choose a random neighbour
                    if state[w] == I:
                        state[v] = I
                        newly_infected[v] = True
        elif random() < s:
            state[v] = S
        if state[v] == R:
            removed[v] = True

    # Filter out the recovered vertices
    g.set_vertex_filter(removed, inverted=True)

    # The following will force the re-drawing of the graph, and issue a
    # re-drawing of the GTK window.
    win.graph.regenerate_surface()
    win.graph.queue_draw()

    # if doing an offscreen animation, dump frame to disk
    if offscreen:
        global count
        pixbuf = win.get_pixbuf()
        pixbuf.savev(r'./frames/sirs%06d.png' % count, 'png', [], [])
        if count > max_count:
            sys.exit(0)
        count += 1

    # We need to return True so that the main loop will call this function more
    # than once.
    return True


# Bind the function above as an 'idle' callback.
cid = GObject.idle_add(update_state)

# We will give the user the ability to stop the program by closing the window.
win.connect("delete_event", Gtk.main_quit)

# Actually show the window, and start the main loop.
win.show_all()
Gtk.main()
