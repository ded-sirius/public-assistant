#!/usr/bin/env python
import re
import googlemaps
from datetime import datetime
from config import GOOGLE_API_KEY

MODE = 'walking'

class Directions:
    def __init__(self, origin, destination):
        self.instructions = []
        self.duration = ''
        self.distance = ''
        self.gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
        self.getDirections(origin, destination)
        self.getInstructions()
        self.setDistance()
        self.setTime()

    def getDirections(self, origin, destination):
        # Request directions via public transit
        now = datetime.now()
        self.directions_result = self.gmaps.directions(origin,
                                             destination,
                                             mode="transit",
                                             departure_time=now)

    def getInstructions(self):
        print config
        print self.directions_result
        steps = self.directions_result[0]['legs'][0]['steps']
        for step in steps:
            instruction = cleanhtml(step['html_instructions'])
            self.instructions.append(instruction)

    def setDistance(self):
        self.distance = self.directions_result[0]['legs'][0]['distance']

    def setTime(self):
        self.duration = self.directions_result[0]['legs'][0]['duration']


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
