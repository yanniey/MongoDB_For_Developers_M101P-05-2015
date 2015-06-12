

import pymongo
import sys


# Copyright 2013, 10gen, Inc.
# Author: Andrew Erlichson


# connnecto to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")



db = connection.m101                 # attach to db
collection = db.funnynumbers         # specify the colllection


magic = 0

try:
    iter = collection.find()
    for item in iter:
        if ((item['value'] % 3) == 0):
            magic = magic + item['value']

except Exception as e:
    print "Error trying to read collection:", type(e), e


print "The answer to Homework One, Problem 2 is " + str(int(magic))


