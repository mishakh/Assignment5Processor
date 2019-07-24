#Assignment 5 ARM Processor
import processor_c as arm

####deconstruct instruction
#for instruc in instrucMem:
#    instruc=instruc.replace(",","")
#    instruc=instruc.split()
#    print(instruc)
#import processor_Classes.py

##
##  op | Rm | shamt | Rn | Rd	= MEM[PC]		R-format
##	op | Imm | Rn | Rd 		    = MEM[PC]		I-format
##	op | addr | op2 | Rn | Rt 	= MEM[PC]		D-format
##	op | addr | Rt 			    = MEM[PC]		CB-format
##	op | addr 	    		    = MEM[PC]		B-format


####INITIAL
#load Instruction Memory
f = open("assignment5.txt", 'r')
instrucMem = f.readlines()
PC=0
Reg=[None]*32

reg=arm.Registers()

####RUN TIME
while(PC<len(instrucMem)):
    NPC=PC+1

    inReg=arm.InstructionReg(instrucMem[PC])   #Instruction Fetch
    controlU=arm.Control()
    controlU.insRead(inReg.opcode)  #Set control bit values

    PC=NPC
#    ExecCalc=arm.ALU(
    #Instruction Deconstruction Occurs in IR constructor function
