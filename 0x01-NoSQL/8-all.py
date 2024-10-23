#!/usr/bin/env python3
"""
Title: List all doc in python
Description: script that lists all documents in a collection:
Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""

import pymongo


def list_all(mongo_collection):
    """ fxn that list all doc """

    documents = mongo_collection.find()

    return [i for i in documents]
