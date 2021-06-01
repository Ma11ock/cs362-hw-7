#!/usr/bin/env python

# by Ryan Jeffrey
# Determines if the year entered is a leap year.

# From the directions:
# Years that are evenly divisible by 4 except
# years that are evenly divisible by 100
# unless the years are also evenly divisible by 400.

def isLeapYr(year: int) -> bool:
    return year % 4 == 0 and (not (year % 100 == 0) or (year % 400 == 0))
