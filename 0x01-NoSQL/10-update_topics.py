#!/usr/bin/env python3
"""
Task 10 Module - Updating documents
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object
        name: (string) the school name to update
        topics: (list of strings) list of topics approached in the school

    Return:
        None
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
