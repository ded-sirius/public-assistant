#!/usr/bin/env python
from lib.directions import Directions

origin = "sunset park"
destination = "UNLV"
directions = Directions(origin, destination)

for instruction in directions.instructions:
    print instruction

print "You will walk for {}, in {}".format(directions.distance['text'], directions.duration['text'])
