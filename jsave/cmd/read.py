import argparse
from ..jsave import JFile, JData

parser = argparse.ArgumentParser(description="read data from a file")

parser.add_argument("file", type=str, help="filename read the data from")
parser.add_argument("--indent", type=int, default=0, help="indent to format the data with, use -1 for no formatting")
args = parser.parse_args()

output_file = JFile(args.file)

print(output_file.read().prettify(args.indent))

