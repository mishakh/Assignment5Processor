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
    addr=0
    def __init__(self, instruc):
        instruc=instruc.replace(",","")     ##format instruction 
        instruc=instruc.replace("#","")     ##for code to read
        instruc=instruc.replace("XZR","0")  ##
        instruc=instruc.replace("X","")     ##
        instruc=instruc.replace("[","")     ##
        instruc=instruc.replace("]","")     ##
        instruc=instruc.split()             #seperate instruction into addressable entities
        self.opcode=instruc[0]
        if(self.opcode=='ADD' or self.opcode=='SUB' or self.opcode=='AND' or self.opcode=='ORR'):
            self.Format='R'
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])
            self.Rm=int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.Rm)
        elif (self.opcode=='LDUR' or self.opcode=='STUR'):
            self.Format='D'
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])
            self.addr= int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.addr)
        elif(self.opcode=='ADDI' or self.opcode=='SUBI'):
            self.Format='I'
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])
            self.Imm=int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.Imm)
        elif(self.opcode=='B' or self.opcode=='CBZ'):
            self.Format='B'
            self.addr=int(instruc[1])
            if(self.opcode=='CBZ'):
                self.Rd=int(instruc[1])
                self.addr=int(instruc[2])
            print(self.opcode, self.Rd, self.addr)

####INITIAL
#load Instruction Memory
f = open("assignment5.txt", 'r')
instrucMem = f.readlines()
PC=0
Reg=[None]*32
        
####RUN TIME
while(PC<len(instrucMem)):
    instructFetch=InstructionReg(instrucMem[PC])   #Instruction Fetch
    NPC=PC+1
    PC=NPC
