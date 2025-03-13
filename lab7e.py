#!/usr/bin/env python3
# Student ID: asaini85

from lab7d import *

class Time(Time):
    def __str__(self):
        """Return string representation for print()."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return representation for interactive shell."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'
