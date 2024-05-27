from build123d import *
import vpype as vp

def is_point_on_segment(px, py, x1, y1, x2, y2):
    collinear = (py - y1) * (x2 - x1) == (y2 - y1) * (px - x1)
    within_bounds = min(x1, x2) < px < max(x1, x2) or min(y1, y2) < py < max(y1, y2)
    return collinear and within_bounds

input = import_svg("input.svg")

exporter = ExportSVG()
exporter.add_layer(name="layer1", line_color=(255,0,0))

# Storing all segment and vertex information on arrays
segments = []
vertices = []

for wire in input:
    for segment in wire.edges():
        segments.append(segment.vertices())
        for vertex in segment.vertices():
            vertices.append(vertex)

# Finding overlapping lines and counting them
counter = 0

for vertex in vertices:
    px = vertex.X
    py = vertex.Y
    for segment in segments:
        x1 = segment[0].X
        y1 = segment[0].Y
        x2 = segment[1].X
        y2 = segment[1].Y
        if is_point_on_segment(px, py, x1, y1, x2, y2):
            counter+=1
    
if counter:
    for segment in segments:
