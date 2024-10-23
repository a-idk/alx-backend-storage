#!/usr/bin/env python3
"""
Title: Schools with specific topic
Description: Python function that returns the list of school
	having a specific topic:
	Prototype: def schools_by_topic(mongo_collection, topic):
	mongo_collection will be the pymongo collection object
	topic (string) will be topic searched11. Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """ fxn that list schools by specific topic """

    return mongo_collection.find({"topics": topic})
