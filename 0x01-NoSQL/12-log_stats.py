#!/usr/bin/env python3
"""
script that provides some stats
about nginx logs stored in mongodb
    Data
"""
from pymongo import MongoClient as mc


def main():
    """main func"""
    with mc() as client:
        db = client.logs
        coll = db.nginx

        no_of_docs = coll.count_documents({})
        print(no_of_docs, "logs")
        print('Methods:')
        no_of_get = coll.count_documents({"method": "GET"})
        print(f'    method GET: {no_of_get}')
        no_of_post = coll.count_documents({"method": "POST"})
        print(f'    method POST: {no_of_post}')
        no_of_put = coll.count_documents({"method": "PUT"})
        print(f'    method PUT: {no_of_put}')
        no_of_patch = coll.count_documents({"method": "PATCH"})
        print(f'    method PATCH: {no_of_patch}')
        no_of_del = coll.count_documents({"method": "DELETE"})
        print(f'    method DELETE: {no_of_del}')
        stat_ck = coll.count_documents({"method": "GET", "path": "/status"})
        print(f'{stat_ck} status check')


if __name__ == "__main__":
    main()
