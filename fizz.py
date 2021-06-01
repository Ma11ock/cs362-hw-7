#!/usr/bin/env python
# FizzBuzz.

def isFizz(arg: int) -> bool:
    if arg % 3 == 0:
        return True
    return False


def isBuzz(arg: int) -> bool:
    if arg % 5 == 0:
        return True
    return False
