# main.py

from command import Command
from takt import *

""" Witch mode use memory """
READING = 0
REG = 0
RAM = 1
CALC = 0
WRITING = 1

commands = []
takts = []

data = open("data.txt", 'r')
for i in data:
    com_type, op2, calc = i.split()
    commands.append(Command(int(com_type), int(op2), int(calc)))
for com in commands:
    com.show()
data.close()



current_takt = Takt(WRITING, RAM, REG, REG, READING)
takt_error = current_takt.is_conflict()

