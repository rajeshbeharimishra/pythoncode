from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

gmap.plot(37.428, -122.145,'cornflowerblue', edge_width=10)

gmap.draw("testmap.html")

