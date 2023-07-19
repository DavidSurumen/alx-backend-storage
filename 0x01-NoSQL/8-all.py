#!/usr/bin/env python3
"""
Task 8 Module - Defines a function 'list_all'
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    Args:
        mongo_collection: collection

    Return:
        lst: List of documents

    """
    lst = []
    for doc in mongo_collection.find():
        lst.append(doc)

    return lst
