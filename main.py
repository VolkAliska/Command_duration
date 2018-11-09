# main.py

from command import Command
from takt import *

""" Witch mode use memory """
READING = 0
REG = 0
RAM = 1
CALC = 0
WRITING = 1

com1 = Command(1, 2, 1)
com2 = Command(2, 5, 4)
current_takt = Takt(WRITING, RAM, REG, REG, READING)
takt_error = current_takt.is_conflict()
com1.show()
com2.show()
