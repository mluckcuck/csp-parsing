#!/usr/bin/python
# -*- coding: utf-8 -*-

from lark import *

class CSP_Walker(object):

    def __init__(self, translator):
        self.translator = translator

    def walk(self, parse_tree):

        for t in parse_tree.children:
            if t.data == 'chan_decl':
                self._walk_chan_decl(t)

            elif t.data == "proc_decl":
                self._walk_proc_decl(t)
            else:
                raise Exception("Not a CSP Node")

    def _walk_chan_decl(self, chan_decl):

        #print(chan_decl)
        children = chan_decl.children
        channel_names = []
        channel_type =""
        for c in children:
            if c.data == "chan_name":
                channel_names.append(str(c.children[0]))
            elif c.data == "chan_type":
                channel_type = c.children[0]

        print(str(channel_names), channel_type)
        #translator.translate_chan_decl(channel_names, channel_type)

    def _walk_proc_decl(self, proc_decl):

        #print(proc_decl)
        children = proc_decl.children
        proc_name = ""
        arguments = []
        proc_body = []
        for c in children:
            #print(c)
            if c.data == "proc_name":
                proc_name = str(c.children[0])
            elif c.data == "arguments":
                for arg in c.children:
                    arguments.append(str(arg))
            elif c.data == "proc_body":
                for statement in c.children:
                    #print(statement)
                    if statement.data == "prefix":
                        proc_body.append( self._walk_prefix(statement) )
                    elif statement.data == "interleave":
                        left_proc, right_proc = statement.children

                        if left_proc.data == "proc_ref" and right_proc.data == "proc_ref":

                            print(left_proc.children[0].children[0])
                            proc_body.append({"interleave": (str(left_proc.children[0].children[0]), str(right_proc.children[0].children[0]) ) })

        print(proc_name, str(arguments), str(proc_body))

    def _walk_prefix(self, prefix_tree):

        prefix =[]
        for child in prefix_tree.children:
            #print(child)
            if child.data == "event":
                prefix.append({"event" : str(child.children[0])})

            elif child.data == "skip":
                prefix.append({"skip": "SKIP"})
            elif child.data == "stop":
                prefix.append({"stop": "STOP"})
            elif child.data == "prefix":
                prefix.append(self._walk_prefix(child))
            #print(prefix)

        #print("return")
        #print(prefix)
        return {"prefix": prefix }
