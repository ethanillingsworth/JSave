import argparse
from ...pickle import PickleFile

parser = argparse.ArgumentParser(description="pickle data into a file")

parser.add_argument("file", type=str, help="filename save the data to")
parser.add_argument("data", type=str, help="data to write to file")

args = parser.parse_args()

output_file = PickleFile(args.file)

output_file.pickle(args.data)