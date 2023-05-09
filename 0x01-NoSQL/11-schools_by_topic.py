#!/usr/bin/env python3
"""
contains function that returns
the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """does what the above comment says"""

    return mongo_collection.find({"topics": topic})
