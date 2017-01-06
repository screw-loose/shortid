from __future__ import absolute_import

# standard
import time
import os

# project
from shortid.encoder import Encoder
from shortid.alphabet import Alphabet


# Ignore all milliseconds before a certain time to reduce the size of the date entropy
# without sacrificing uniqueness. This number should be updated every year or so to keep
# the generated id short. To regenerate `new Date() - 0` (Javascript) and bump the version.
# Always bump the version!
#
# last updated: Jan 6, 2017
REDUCE_TIME = 1483723562783

# don't change unless we change the algos or REDUCE_TIME
# must be an integer and less than 16
#
# last updated: Jan 6, 2017
VERSION = 3


class ShortId(object):
    def __init__(self):
        self._counter = 0
        self._previous_delta = 0
        self._encoder = Encoder()
        self._alphabet = Alphabet()

    def generate(self):
        delta = self._get_time_delta()

        if delta == self._previous_delta:
            self._counter += 1
        else:
            self._counter = 0
            self._previous_delta = delta

        res = self._encoder.encode(self._alphabet.lookup, VERSION)
        res = res + self._encoder.encode(self._alphabet.lookup, os.getpid())

        if self._counter > 0:
            res = res + self._encoder.encode(self._alphabet.lookup, self._counter)

        res = res + self._encoder.encode(self._alphabet.lookup, delta)

        return res

    def _get_time(self):
        return int(time.time() * 1000)

    def _get_time_delta(self):
        return int(round((self._get_time() - REDUCE_TIME) * 0.01))
