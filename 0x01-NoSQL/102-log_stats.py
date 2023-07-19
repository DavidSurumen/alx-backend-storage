#!/usr/bin/env python3
"""
Task 102 Module - script that provides stats about Nginx logs
stored in MongoDB
"""
from pymongo import MongoClient
from collections import Counter


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

    # display methods summary
    print('{} logs'.format(logs_num))
    print('Methods:')

    for m in method:
        print('\tmethod {}: {}'.
              format(m, coll.count_documents({'method': m})))

    print('{} status check'.format(count_get))

    # get list of all IP occurrences in the dataset
    ips_list = [doc.get('ip') for doc in coll.find()]

    # get top 10 of most present IPs
    top_ten = Counter(ips_list).most_common(10)

    # dispay IPs summary
    print('IPs:')
    for ip in top_ten:
        print('\t{}: {}'.format(ip[0], ip[1]))
