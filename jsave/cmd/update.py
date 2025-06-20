import argparse
from ..jsave import JFile, JData

parser = argparse.ArgumentParser(description="save data to a file")

parser.add_argument("file", type=str, help="file to update")
parser.add_argument("key", type=str or int, help="key path to update")
parser.add_argument("value", help="value to put at key path")


args = parser.parse_args()
file = JFile(args.file)

file.update(args.key, args.value)
