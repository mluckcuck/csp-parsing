#!/usr/bin/python
# -*- coding: utf-8 -*-

class Channel_Decl(object):

    def __init__(self, name, type_list):
        self.name = name
        self.type_list = type_list

    def __str__(self):

        if type_list != None:

            head, *tail = type_list
            types = head
            for type in tail:
                types += ", " + type


            return "channel " + name +  " : " + types
        elif type_list:
            return "channel " + name

class Proc_Decl(object):

    def __init__(self, proc_name, parameters, proc_body):
        self.proc_name = proc_name
        self.parameters = parameters
        self.proc_body = proc_body




class CSP(object):

    def __init__(self):
        self.channels = []
        self.processes = []

    def add_channel(self, channel):
        self.channels.append(channel)
