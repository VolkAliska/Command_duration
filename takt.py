# takt.py

""" Witch mode use memory """
READING = 0
REG = 0
RAM = 1
CALC = 0
WRITING = 1

class Takt():

    ops = []

    def __init__(self, op0, op1, op2, op3, op4):
        """ Operations 0...4 running now """
        self.ops = [op0, op1, op2, op3, op4]

    def is_conflict(self):
        if self.ops.count(1) > 1 in self.ops:
            return 1

