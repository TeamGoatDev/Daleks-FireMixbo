#!/usr/bin/python
# -*- coding: utf-8 -*-
#Python 3.x
from Enum import *

class ReturnCodes():
    INVALID_MOVE   = Enum.addId()
    INVALID_ACTION = Enum.addId()
    DEAD_DOCTOR    = Enum.addId()
    END_TURN       = Enum.addId()
    SUCCESS	       = Enum.addId()
    END_WAVE	   = Enum.addId()
