# command.py

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
        time.append(1)
        return time
