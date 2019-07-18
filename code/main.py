from enum import Enum


class ALU_opcode(Enum):
    ADD = 1
    SUB = 2


class ALU():
    def __init__(self):
        self.input_A = 0
        self.input_B = 0
        self.output = 0
    def execute_instruction(self,in_a,in_b,op_code):
        self.input_A = in_a
        self.input_B = in_b

        if( op_code == ALU_opcode.ADD):
            # ADD TWO INPUTS and output  the sum
            self.addition()
        if (op_code == ALU_opcode.SUB):
            # Subtract TWO INPUTS and output the difference
            self.subtract()

    def addition(self):
        self.output = self.input_A + self.input_B

    def subtract(self):
        self.output = self.input_A + self.input_B


class proccessor():
    def __init__(self):
        self.program_counter = 0

        self.General_AUL = ALU()






def decode_instruction():
    pass
