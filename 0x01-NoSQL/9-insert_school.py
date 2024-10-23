#!/usr/bin/env python3
"""
Title: Insert a doc in Python
Description: Python function that inserts a new document in a collection
	based on kwargs:
	Prototype: def insert_school(mongo_collection, **kwargs):
	mongo_collection will be the pymongo collection object
	Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """ fxn that inserts a new doc """

    new = mongo_collection.insert_one(kwargs)

    return new.inserted_id
