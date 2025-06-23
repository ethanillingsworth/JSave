import argparse
from ...jsave import JFile, JData, StringList

parser = argparse.ArgumentParser(description="read data from a file")

parser.add_argument("file", type=str, help="filename read the data from")
parser.add_argument("-k", "--key", action="append", help="add key to read from the file")
parser.add_argument("--indent", type=int, default=4, help="indent to format the data with, use -1 for no formatting")
parser.add_argument("--safe-mode", action=argparse.BooleanOptionalAction, help="toggle safe mode on or off")
args = parser.parse_args()

output_file = JFile(args.file)
if (args.key):
    args.key = StringList(args.key)
    print(output_file.read(args.key, args.safe_mode).prettify(args.indent))
else:
    print(output_file.read().prettify(args.indent))

