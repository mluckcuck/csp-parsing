#!/usr/bin/python
# -*- coding: utf-8 -*-



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
parseTree = parser.parse(SOURCE)

if PRINT:
    print("+++ Pretty Parse Tree +++")
    print("")

    print(parseTree.pretty())
    print("")

print("+++ Translator Output +++")
print("")

if TRANSLATOR == "test":
    # Just Prints the Output, which should be the same (apart from whitespace)
    # as the input
    test_trans = Test_Translator()
    print(test_trans.translate(parseTree))

elif TRANSLATOR == "rosmon_rml":
    romMon_trans = ROSMon_Translator()
    rosmon_config = romMon_trans.translate(parseTree)

    print(rosmon_config)

    output_file = open(OUTPUT_PATH, "w")
    output_file.write(rosmon_config)
    output_file.close()


print("")
