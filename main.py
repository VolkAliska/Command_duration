# main.py

from command import *


commands = []

data = open("data.txt", 'r')
for i in data:
    com_type, op2, calc = i.split()
    commands.append(Command(int(com_type), int(op2), int(calc)))
data.close()

i = 0
for com in commands:
    com.norm_time(i)
    i += 1

for i in range(1, len(commands)):
    for j in range(0, i):
        com_cmp(commands[i], commands[j])

for com in commands:
    com.show_work_version()

print("res")
for com in commands:
    com.show_res_version()

max_time = 0
for com in commands:
    max_time += len(com.time)

print(max_time)
av_time = max_time / len(commands)
print(av_time)