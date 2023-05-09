#!/usr/bin/env python3
"""
contains a function thatr changes all topics
of a school doc based on the name
"""


def update_topics(mongo_collection, name, topics):
    """does what the top comment syas"""
    res_obj = mongo_collection.update_many({"name": name},
                                           {"$set": {"topics": topics}})
