#!/usr/bin/python3
"""Python function to create class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dic[key] = value
        return dic

    def reload_from_json(self, json):
        ''' method that replaces all atrributes of the Student instance'''

        for j_key, j_value in json.items():
            self.__dict__[j_key] = j_value
