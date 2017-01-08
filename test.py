#!/usr/bin/env python
from lib.directions import Directions

origin = "6795 S Edmond St #110, Las Vegas, NV 89118"
destination = "UNLV"
directions = Directions(origin, destination)

for instruction in directions.instructions:
    print instruction

print "You will walk for {}, in {}".format(directions.distance['text'], directions.duration['text'])
