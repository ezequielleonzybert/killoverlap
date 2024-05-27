from build123d import *

input = import_svg("test.svg")

with BuildLine() as lines:
    for edge in input.edges():
        add(edge)

shape = lines._obj

exporter = ExportSVG()
exporter.add_layer(name="layer1", line_color=(255,0,0),line_weight=1)
exporter.add_shape(shape,"layer1")
exporter.write("output.svg")