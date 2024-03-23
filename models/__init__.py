#!/usr/bin/python3
""" The initialization of BaseModel class """


class BaseModel:
    """ The base class"""
    def __init__(self, my_number, name, updated_at, id, created_at):
        self.my_number = my_number
        self.name = name
        self.updated_at = updated_at
        self.id = id
        self.created_at = created_at
