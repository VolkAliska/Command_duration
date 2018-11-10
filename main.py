# main.py

from command import *
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
data.close()

i = 0
for com in commands:
    com.norm_time(i)
    com.show()
    i += 1

for i in range(1, len(commands)):
    for j in range(0, i):
        com_cmp(commands[i], commands[j])

commands[0].time.append(1)
for i in range(1, len(commands)):
    for j in range(0, i):
        time_cmp(commands[i], commands[j])

for com in commands:
    com.show()

current_takt = Takt(WRITING, RAM, REG, REG, READING)
takt_error = current_takt.is_conflict()

