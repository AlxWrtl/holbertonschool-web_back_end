#!/usr/bin/env python3
"""Function that lists all documents in a collection"""


def list_all(mongo_collection):
    """list all documents in collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
