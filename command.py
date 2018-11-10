# command.py


def com_cmp(com1, com2):
    """ Compare 1 in the similar takts and insert 3 instead "no operation" """
    for i in range(0, min(len(com1.time), len(com2.time))):
        if (com1.time[i] == 1) and (com1.time[i] == com2.time[i]):
            com1.time.insert(i, 3)


def time_cmp(com1, com2):
    """ Append 1 in the end like "writing", 4 if needed like "no operation" """
    flag = 0
    while 1:
        if flag == 1:
            break
        if len(com2.time)-1 > len(com1.time):
            if (com2.time[len(com1.time)-1] == 1 or com2.time[len(com1.time)-1] == 4) and com1.time[len(com1.time)-1] != 1:
                com1.time.append(4)
            elif (com2.time[len(com1.time)-1] == 1 or com2.time[len(com1.time)-1] == 4) and com1.time[len(com1.time)-1] == 1:
                com1.time.insert(len(com1.time)-1, 4)
            else:
                if com1.time[len(com1.time) - 1] == 1:
                    break
                com1.time.append(1)
                flag = 1
        else:
            if com1.time[len(com1.time) - 1] == 1:
                break
            com1.time.append(1)
            flag = 1


class Command():
    def __init__(self, com_type, op2, calc):
        self.type = com_type
        self.read = 1
        self.op1 = 1
        self.op2 = op2
        self.calc = calc
        self.write = 1
        self.time = self.get_time()

    def show(self):
        description = 'Type: {}, read: {}, op1: {}. op2: {}, calc: {}, write: {}\n time: {}\n mem: {}'\
            .format(self.type, self.read,
                    self.op1, self.op2,
                    self.calc, self.write,
                    len(self.time), self.time)
        print(description)

    def get_time(self):
        """" Command working process: 1 - use memory """
        time = [0, 0]
        for i in range(0, self.op2):
            time.append(1)
        for i in range(0, self.calc):
            time.append(0)
        #time.append(1) for correct working insert 1 for writing later
        return time

    def norm_time(self, i):
        """ Insert unusable 2 into the left """
        for j in range(0, i):
            self.time.insert(0, 2)

