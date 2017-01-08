#!/usr/bin/env python
import re
import googlemaps
from datetime import datetime
from config import GOOGLE_API_KEY

MODE = 'walking'

class Directions:
    def __init__(self, origin, destination):
        self.instructions = []
        self.time = 0
        self.distance = 0
        self.gmaps = googlemaps.Client(key=GOOGLE_API_KEY)
        self.getDirections(origin, destination)
        self.getInstructions()

    def getDirections(self, origin, destination):
        # Request directions via public transit
        now = datetime.now()
        self.directions_result = self.gmaps.directions(origin,
                                             destination,
                                             mode="transit",
                                             departure_time=now)

    def getInstructions(self):
        steps = self.directions_result[0]['legs'][0]['steps']
        for step in steps:
            instruction = cleanhtml(step['html_instructions'])
            self.instructions.append(instruction)

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
