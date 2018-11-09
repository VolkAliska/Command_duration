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
        description = 'Type: {}, read: {}, op1: {}. op2: {}, calc: {}, write: {}\n time: {}'\
            .format(self.type, self.read,
                    self.op1, self.op2,
                    self.calc, self.write, self.time)
        print(description)

    def get_time(self):
        """" Command working time """
        time = self.read + self.op1 + self.op2 + self.calc + self.write
        return time
