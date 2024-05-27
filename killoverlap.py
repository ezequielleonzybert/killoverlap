from build123d import *
import argparse

def main(input_file, output_file, join):
    input = import_svg(input_file)

    if join:
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process SVG files.')
    parser.add_argument('input_file', type=str, help='Path to the input SVG file.')
    parser.add_argument('output_file', type=str, help='Path to the output SVG file.')
    parser.add_argument('--join', action='store_true', help='Enable the join feature.')
    
    args = parser.parse_args()
    
    main(args.input_file, args.output_file, args.join)