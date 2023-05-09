#!/usr/bin/env python3
"""
contains a new function that inserts a new doc
in col based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """returns the new _id"""
    res_obj = mongo_collection.insert_one(kwargs)

    return res_obj.inserted_id

