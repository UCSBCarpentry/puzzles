#! /usr/bin/python

# Writes selected columns from an Excel-dialect CSV file to standard
# output.  The output is also in CSV format unless an output delimiter
# is specified, in which case the delimiter is used and there is no
# escaping mechanism.  Invoke with -h for usage.
#
# Greg Janee <gregjanee@gmail.com>
# January 2019

import argparse
import csv
import re
import sys

def error (exceptionType, exception, traceback):
  sys.stderr.write("%s: %s\n" % (sys.argv[0], str(exception)))
  sys.exit(1)
sys.excepthook = error

def columnRange (s):
  if s == "*": s = "1-"
  try:
    m = re.match("(\d+)(-(\d+)?)?$", s)
    i = int(m.group(1))
    assert i > 0
    if m.group(2) == None:
      j = i
    else:
      if m.group(3) == None:
        j = None
      else:
        j = int(m.group(3))
        assert j >= i
  except:
    raise argparse.ArgumentTypeError("not of the form n, n-, m-n, or *")
  return (i-1, j)

p = argparse.ArgumentParser(description="Cuts columns from a CSV file.")
p.add_argument("-d", metavar="DELIMITER", dest="delimiter",
  help="output delimiter")
p.add_argument("-i", dest="ignoreErrors", action="store_true",
  help="ignore occurrences of DELIMITER in column values")
p.add_argument("inputFile", metavar="{input.csv or -}",
  help="input file or standard input")
p.add_argument("columnRanges", metavar="columns", nargs=argparse.REMAINDER,
  type=columnRange,
  help="columns to output, repeatable: n (single column), " +\
  "m-n (column range), n- (open ended range), * (all columns)")
args = p.parse_args(sys.argv[1:])

if args.inputFile == "-":
  reader = csv.reader(sys.stdin)
else:
  reader = csv.reader(open(args.inputFile))
if args.delimiter == None: writer = csv.writer(sys.stdout)

for row in reader:
  r = []
  for i, j in args.columnRanges:
    assert i < len(row) and (j == None or j <= len(row)),\
      "column reference exceeds number of columns"
    r.extend(row[i:j])
  if args.delimiter == None:
    writer.writerow(r)
  else:
    assert args.ignoreErrors or not any(args.delimiter in v for v in r),\
      "delimiter occurs in column value"
    sys.stdout.write(args.delimiter.join(r) + "\n")
