from build123d import *
import argparse

def main(input_file, output_file, j):
    input = import_svg(input_file)

    if j:
        with BuildSketch() as sketch:
            with BuildLine() as lines:
                for edge in input.edges():
                    add(edge)
                add(lines._obj)
        shape = sketch.consolidate_edges()
    else:
        with BuildLine() as lines:
                for edge in input.edges():
                    add(edge)
        shape = lines._obj

    exporter = ExportSVG()
    exporter.add_layer(name="layer1", line_color=(255,0,0),line_weight=1)
    exporter.add_shape(shape,"layer1")
    exporter.write(output_file)

def runner():
    parser = argparse.ArgumentParser(description='Find and merge all overlapping lines in an SVG drawing.')
    parser.add_argument('input_file', type=str, help='Path to the input SVG file.')
    parser.add_argument('output_file', type=str, help='Path to the output SVG file.')
    parser.add_argument('-j', action='store_true', help='Join all connected lines into a wire.')
    
    args = parser.parse_args()
    
    main(args.input_file, args.output_file, args.j)