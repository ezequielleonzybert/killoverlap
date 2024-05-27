from build123d import *

input = import_svg("input.svg")

with BuildPart() as part:
    for edge in input.edges():
        add(edge)

shape = part.pending_edges_as_wire

exporter = ExportSVG()
exporter.add_layer(name="layer1", line_color=(255,0,0))
exporter.add_shape(shape,"layer1")
exporter.write("output.svg")