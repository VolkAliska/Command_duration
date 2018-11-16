# main.py


from command import *
from data_input import *

p_k = get_pk()
p_op2 = get_pop2()
num = input('Enter number of commands\n')
pam = input('Enter time value for reading the second operand: 2, 5, 10\n')
calc = input('Enter time value for calculation: 4, 8, 16\n')

data = open("data.txt", 'w')
data.close()
for i in range(0, int(num)):
    com = generate_command(p_k, p_op2, calc, pam)

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

# print(max_time)
av_time = max_time / len(commands)
print("\n\nAverage time:")
print(av_time)
