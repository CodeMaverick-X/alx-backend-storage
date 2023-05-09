#!/usr/bin/env python3
"""
contains function that returns all
students sorted by average score
"""


def top_students(mongo_collection):
    """does what is in the above comment
    """
    return mongo_collection.aggregate(
        [{"$project": {"_id": "$_id", "name": 1,
                       "averageScore": {"$avg": "$topics.score"}},
          },
         {"$sort": {"averageScore": -1}}
         ])
