#!/usr/bin/env python3
"""
Task 12 Module - script that provides stats about Nginx logs
stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # create connection object
    client = MongoClient('mongodb://127.0.0.1:27017')
    coll = client.logs.nginx

    # get documents count
    logs_num = coll.count_documents({})

    # declare methods
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # get count of documents with method=GET and path=/status
    count_get = coll.count_documents({'method': 'GET', 'path': '/status'})

    # display
    print('{} logs'.format(logs_num))
    print('Methods:')
    for m in method:
        print('\tmethod {}: {}'.
              format(m, coll.count_documents({'method': m})))

    print('{} status check'.format(count_get))
