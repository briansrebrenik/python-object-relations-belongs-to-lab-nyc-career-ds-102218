# import car class here
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def occupation(self):
        return self._occupation
    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation

    @classmethod
    def has_oldest_car(cls):
        dict = {}
        for car in Car._all:
            dict[car.owner.name] = car.year
        return min(dict, key=dict.get)

    @classmethod
    def drives_a(cls, make):
        return [car.owner for car in Car._all if car.make == make]


    def drives_same_make_as_me(self):
        my_car = list(filter(lambda car: car.owner == self, Car._all))
        return [car.owner.name for car in Car._all if car.make == my_car[0].make and car.owner != my_car[0].owner]
