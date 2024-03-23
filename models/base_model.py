#!/usr/bin/python3
import uuid
import datetime
"""a class BaseModel that defines
all common attributes/methods for other classes"""


class BaseModel:
    """This is the base class of the entire application

    name: BaseModel"""
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """ A module that prints
        [<class name>] (<self.id>) <self.__dict__> """
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """ A method to update public instance attribute
        updated_at with the current datetime """

        BaseModel.updated_at = datetime.datetime.now()
        print("This model was updated at: {}".format(BaseModel.updated_at))

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """

        for key, value in self.__dict__:
            print(key, value)


print("Does my code work?")
print()
the_model = BaseModel()
print()
print(the_model)
print()
print(str(the_model))
the_model.to_dict()
print()
the_model.save()
