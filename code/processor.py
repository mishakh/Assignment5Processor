#Assignment 5 ARM Processor
import processor_c as arm
<<<<<<< HEAD
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


=======
>>>>>>> 10a74173e409a51a5b3386e0fe08e0541fcbee67

####INITIAL
#load Instruction Memory
f = open("assignment5.txt", 'r')
instrucMem = f.readlines()
PC=0
<<<<<<< HEAD
Reg=[None]*32
=======
reg=arm.Registers()
>>>>>>> 10a74173e409a51a5b3386e0fe08e0541fcbee67

####RUN TIME
while(PC<len(instrucMem)):
    NPC=PC+1
    
    inReg=arm.InstructionReg(instrucMem[PC])   #Instruction Fetch
    controlU=arm.Control()          
    controlU.insRead(inReg.opcode)  #Set control bit values
    
    PC=NPC
#    ExecCalc=arm.ALU(
    #Instruction Deconstruction Occurs in IR constructor function

