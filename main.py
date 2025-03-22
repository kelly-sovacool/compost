#!/usr/bin/env python
from noaa_sdk import NOAA
from pprint import pprint

n = NOAA()
observations = n.get_observations('48242','US',start='2024-03-15',end='2025-03-17')
for observation in observations:
    pprint(observation)
    break
