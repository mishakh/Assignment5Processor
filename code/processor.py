#Assignment 5 ARM Processor
import processor_c as arm

####INITIAL
#load Instruction Memory
f = open("assignment5.txt", 'r')
instrucMem = f.readlines()
PC=0
Reg=[None]*32
        
####RUN TIME
while(PC<len(instrucMem)):
    instructFetch=arm.InstructionReg(instrucMem[PC])   #Instruction Fetch
    NPC=PC+1
    PC=NPC
    if
#    ExecCalc=arm.ALU(
    #Instruction Deconstruction Occurs in IR constructor function

