#!/usr/bin/env python3
"""
Task 11 Module - Defines the function 'schools_by_topic'
"""


def schools_by_topic(mongo_collection, topic):
    """
    Gets a list of schools having a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic: a topic to filter by

    Return:
        list of schools
    """
    schools = []
    for schl in mongo_collection.find({'topics': topic}):
        schools.append(schl)
    return schools
