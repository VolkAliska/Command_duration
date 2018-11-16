# data_input.py

import numpy as np
import random


def get_pk():
    pk = input('Enter the probability (P) that the command type is 1: 0.9, 0.7, 0.5\n')
    return pk


def get_pop2():
    p_op2 = input('Enter the probability (P) that the second operator is REGISTER: 0.9, 0.8, 0.6\n')
    return p_op2


def generate_command(p_k, p_op2):
    data = open("data.txt", 'a')
    t = [1, 2]
    com_type = np.random.choice(t, p=[float(p_k), 1 - float(p_k)])
    if com_type == 2:
        t = [4, 8, 16]
        com_calc = random.choice(t)
    else:
        com_calc = 1
    op2 = [1, 2] # 1 - reg, 2 - mem
    com_op2 = np.random.choice(op2, p=[float(p_op2), 1 - float(p_op2)])
    if com_op2 == 2:
        t = [2, 5, 10]
        com_op2 = random.choice(t)
    command = [type, com_op2, com_calc]
    data.write('{} {} {}\n'.format(com_type, com_op2, com_calc))
    data.close()
    return command