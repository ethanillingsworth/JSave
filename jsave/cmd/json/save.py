import argparse
from ...jsave import JFile, JData

parser = argparse.ArgumentParser(description="save data to a file")

parser.add_argument("file", type=str, help="filename to save the data to -- if no args are specified the file will be created with no data")
parser.add_argument("-c", "--clone", type=str, help="clone data from another file to the output file")
parser.add_argument("-i", "--input", help="data to save to file, dict or list")
parser.add_argument("--indent", type=int, default=4, help="indent to format the file with")
args = parser.parse_args()

output_file = JFile(args.file)

output_file.create()

if (args.clone):
    output_file.save(JFile(args.clone).read(), args.indent)

if (args.input):
    output_file.save(JData(args.input), args.indent)
