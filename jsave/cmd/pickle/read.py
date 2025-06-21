import argparse
from ...pickle import PickleFile

parser = argparse.ArgumentParser(description="read data from a file")

parser.add_argument("file", type=str, help="filename read the data from")
args = parser.parse_args()

output_file = PickleFile(args.file)

print(output_file.unpickle())