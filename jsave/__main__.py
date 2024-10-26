import argparse
from jsave import JFile, JData
from colorxs import Color
from jsave.error import Error
import json
from jsave.utils import clear

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--save", dest="save", help="Save", action="store_true")
parser.add_argument("-r", "-l", "--read", dest="read", help="Read", action="store_true")
parser.add_argument("-o", "--output", dest="output", help="Text to Write to File", type=str)
parser.add_argument("-f", "--file", dest="file", help="File path", default="file.json", type=str)

args = parser.parse_args()

file = JFile(args.file)

if args.save:
    if not args.output:
        Error(2001, "-o or --output isnt specified!", True)
    try:
        file.save(JData(args.output))
        print(f"Wrote\n{JData(args.output).prettify()}\nto {args.file}")
    except json.decoder.JSONDecodeError:
        Error(2002, "Output isnt a valid JSON!", True)

if args.read:
    clear()
    print(file.read().prettify())
