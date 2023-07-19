#!/usr/bin/env python3
"""
Task 9 Module - defines the function 'insert_school'
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection

    Args:
        kwargs: dictionary document

    Return:
        inserted_id
    """
    InsertOneResult = mongo_collection.insert_one(kwargs)
    return InsertOneResult.inserted_id
