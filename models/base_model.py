#!/usr/bin/python3
"""a class BaseModel that defines all common attributes/methods for other classe"""


class BaseModel:
    """This is the base class of the entire application

    name: BaseModel"""
    id = uuid.uuid4()
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __str__(self):
        """ A module that prints
        [<class name>] (<self.id>) <self.__dict__> """

        print(self.name)
        print(self.id)
        print(self.__dict__)
    
    def save(self):
        """ A method to update public instance attribute
        updated_at with the current datetime """

        BaseModel.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """

        self.__dict__ = self

