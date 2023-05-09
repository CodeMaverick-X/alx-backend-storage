#!/usr/bin/env python3
"""
script that provides some stats
about nginx logs stored in mongodb
    Data
"""
from pymongo import MongoClient


def main():
    """main func: entry point"""
    with MongoClient() as client:
        db = client.logs
        coll = db.nginx

        no_of_docs = coll.count_documents({})
        print(no_of_docs, "logs")
        print('Methods:')
        no_of_get = coll.count_documents({"method": "GET"})
        print('    method GET: {}'.format(no_of_get))
        no_of_post = coll.count_documents({"method": "POST"})
        print('    method POST: {}'.format(no_of_post))
        no_of_put = coll.count_documents({"method": "PUT"})
        print('    method PUT: {}'.format(no_of_put))
        no_of_patch = coll.count_documents({"method": "PATCH"})
        print('    method PATCH: {}'.format(no_of_patch))
        no_of_del = coll.count_documents({"method": "DELETE"})
        print('    method DELETE: {}'.format(no_of_del))
        stat_ck = coll.count_documents({"method": "GET", "path": "/status"})
        print('{} status check'.format(stat_ck))


if __name__ == "__main__":
    main()
