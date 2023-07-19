#!/usr/bin/env python3
"""
Task 14 Module - Defines the function 'top_students'
"""


def top_students(mongo_collection):
    """
    Produces a list of all students sorted by average score.

    Args:
        mongo_collection: pymongo collection object

    Return:
        sorted list of students
    """
    students = []

    # compute average scores for each student
    for stud in mongo_collection.find():
        sum_score = 0
        topics = stud.get('topics')

        for topic in topics:
            sum_score += topic.get('score')

        avg = sum_score / len(topics)
        stud['averageScore'] = avg

        # append to students array
        students.append(stud)

    return sorted(students, key=lambda x: x['averageScore'], reverse=True)
