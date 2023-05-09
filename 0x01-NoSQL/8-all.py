#!/usr/bin/env python3
"""
contains function that lists all docs in a coll
"""
import pymongo

def list_all(mongo_collection):
    """lists all docs in a coll"""
    coll_lst = []
    for doc in mongo_collection.find():
        coll_lst += [doc]

    return coll_lst
