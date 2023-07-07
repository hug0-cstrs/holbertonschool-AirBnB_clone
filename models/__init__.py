#!/usr/bin/python3
"""init package"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

storage = FileStorage()
storage.reload()

a = 'BaseModel'
b = 'User'
c = 'Place'
d = 'State'
e = 'City'
f = 'Amenity'
g = 'Review'

a1 = BaseModel
b1 = User
c1 = Place
d1 = State
e1 = City
f1 = Amenity
g1 = Review
theClasses = {a: a1, b: b1, c: c1, d: d1, e: e1, f: f1, g: g1}
