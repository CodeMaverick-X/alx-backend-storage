#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the
top 10 of the most present IPs in the ::help from `jude`
collection nginx of the database logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    cl = MongoClient('mongodb://127.0.0.1:27017')
    nginx = cl.logs.nginx

    print("{:d} logs".format(nginx.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {:d}".
              format(method,
                     nginx.count_documents({"method": method})))
    print("{:d} status check".format(
        nginx.count_documents({"method": "GET", "path": "/status"})))
    print("IPs:")
    ips = nginx.aggregate(
        [{"$group": {"_id": "$ip",
                     "count": {"$sum": 1},
                     "totalValue": {"$sum": "$value"}
                     },
          },
         {"$sort": {"count": -1}},
         {"$limit": 10}
         ])
    for do in ips:
        print("\t{}: {:d}".format(do.get('_id'), do.get('count')))
