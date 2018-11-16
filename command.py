# command.py


def com_cmp(com1, com2):
    """ Compare 1 in the similar takts and insert 3 instead "no operation" """
    first1 = com1.time.index(1);
    minlen = min(len(com1.time), len(com2.time))
    count = minlen
    i = 0
    while count > 0:
        count = count - 1
        if (com1.time[i] == 1) and (com1.time[i] == com2.time[i]):
            com1.time.insert(first1, 3)
            count = count + 1
        if i < min(len(com1.time), len(com2.time)) - 1:
            i = i + 1


class Command():
    def __init__(self, com_type, op2, calc):
        self.type = com_type
        self.read = 1
        self.op1 = 1
        self.op2 = op2
        self.calc = calc
        self.write = 1
        self.time = self.get_time()

    def show_work_version(self):
        description = 'Type: {}, read: {}, op1: {}. op2: {}, calc: {}, write: {}\n time: {}\n mem: {}'\
            .format(self.type, self.read,
                    self.op1, self.op2,
                    self.calc, self.write,
                    len(self.time), self.time)
        print(description)

    def show_res_version(self):
        if self.op2 == 1:
            op2property = 'REG'
        else:
            op2property = 'P'

        not_op_count = 0
        not_op_count_2 = 0

        read_f = 0
        op1_f = 0
        op2_f = 0
        for i in self.time:
            if i == 0 and read_f == 0:
                read_f = 1
                continue
            if i == 0 and op1_f == 0:
                op1_f = 1
                continue
            if i == 3 and op2_f == 0:
                not_op_count += 1
                continue
            if i == 1 or i == 0 and op1_f == 1:
                op2_f = 1
                continue
            if i == 3 and op2_f == 1:
                not_op_count_2 += 1
                continue

        description = 'Type: {}, read: {}, op1 - REG: {}, "not operation": {}, op2 - {} : {}, calc: {},' \
                      ' "not operation": {}, write: {}\n time: {}'\
            .format(self.type, self.read,
                    self.op1, not_op_count,
                    op2property, self.op2,
                    self.calc, not_op_count_2,
                    self.write, len(self.time))
        print(description)

    def get_time(self):
        """" Command working process: 1 - use memory """
        time = [0, 0]
        for i in range(0, self.op2):
            if self.op2 == 1:
                time.append(0)
            else:
                time.append(1)
        for i in range(0, self.calc):
            time.append(0)
        time.append(1)
# time.append(1) for correct working insert 1 for writing later
        return time

    def norm_time(self, i):
        """ Insert unusable 2 into the left """
        for j in range(0, i):
            self.time.insert(0, 2)

