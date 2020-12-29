#!/usr/bin/python
# -*- coding: utf-8 -*-

from walkers.cspm_walker import CSP_Walker # but this only works in Python3

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass
from lark import Lark
import argparse
import os


VERSION_NUM = 0.1

## Arguments
argParser = argparse.ArgumentParser()
argParser.add_argument("grammar", help="The grammar to parse with.", default = "csp")
argParser.add_argument("source", help="The contract file to be parsed.")


## Parse the Args
args = argParser.parse_args()

grammar_loc = "grammars/" + args.grammar +".lark"

GRAMMAR = open(grammar_loc).read()
SOURCE = open(args.source).read()
PRINT = True
TRANSLATOR = None



print("++++++++++++++++++++++++++++++++++++++++++++++")
print("+++++++++++++++++ CSP Parser +++++++++++++++++")
print("++++++++++++++++ version " + str(VERSION_NUM) + " +++++++++++++++++")
print("+++++++++++++++ Matt Luckcuck ++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++")
print("")




## Add the GRAMMAR to the parser
parser = Lark(GRAMMAR)

print("+++ Input File = +++")
print(SOURCE)
print("")

#Parse the contract
parse_tree = parser.parse(SOURCE)

if PRINT:
    print("+++ Pretty Parse Tree +++")
    print("")

    print(parse_tree.pretty())
    print("")

print("+++ Translator Output +++")
print("")

if args.grammar == "csp":
    walker = CSP_Walker(None)
    walker.walk(parse_tree)

if TRANSLATOR == "test":
    # Just Prints the Output, which should be the same (apart from whitespace)
    # as the input
    test_trans = Test_Translator()
    print(test_trans.translate(parse_tree))

elif TRANSLATOR == "rosmon_rml":
    romMon_trans = ROSMon_Translator()
    rosmon_config = romMon_trans.translate(parse_tree)

    print(rosmon_config)

    output_file = open(OUTPUT_PATH, "w")
    output_file.write(rosmon_config)
    output_file.close()


print("")
