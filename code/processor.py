#Assignment 5 ARM Processor

####deconstruct instruction
#for instruc in instrucMem:
#    instruc=instruc.replace(",","")
#    instruc=instruc.split()
#    print(instruc)
#import processor_Classes.py

##
##      op | Rm | shamt | Rn | Rd	= MEM[PC]		R-format
##	op | Imm | Rn | Rd 		= MEM[PC]		I-format
##	op | addr | op2 | Rn | Rt 	= MEM[PC]		D-format
##	op | addr | Rt 			= MEM[PC]		CB-format
##	op | addr 	    		= MEM[PC]		B-format

class InstructionReg:
    opcode=0
    Format=''
    Rd=0
    Rn=0
    Rm=0
    Imm=0
    shamt=0
    address=0
    def __init__(self, instruc):
        instruc=instruc.replace(",","")
        instruc=instruc.split()
        self.opcode=instruc[0]
        if(self.opcode=='ADD'|'SUB'|'AND'|'ORR'):
            Format='R'
        Rd=instruc[1]
        Rn=instruc[2]
        Rm=instruc[3]
        print(opcode,Rd,Rn,Rm)
def main():
####INITIAL
#load Instruction Memory
    f = open("assignment5.txt", 'r')
    instrucMem = f.readlines()
    PC=0
    Reg=[None]*32
    for i in range(0,31):
        Reg.append(0)
        
####RUN TIME
#    while(instrucMem[]!='END'):
#        instruc=InstructionReg(instrucMem[PC])   #Instruction Fetch
#        NPC=PC++

