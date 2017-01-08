#!/usr/bin/env python
import re
import googlemaps
from datetime import datetime

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def getDirections(origin, destination, maxDistance=0):
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("6795 S Edmond St #110, Las Vegas, NV 89118",
                                         "UNLV",
                                         mode="transit",
                                         departure_time=now)

def getTextDirections(gDirections):
    directions = []
    steps = gDirections[0]['legs'][0]['steps']
    # output starting direction
    #directions.append(steps['html_instructions'])
    for step in steps:
        instruction = cleanhtml(step['html_instructions'])
        print instruction
    return directions

