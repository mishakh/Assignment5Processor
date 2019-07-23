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
    NPC=PC+1
    
    inReg=arm.InstructionReg(instrucMem[PC])   #Instruction Fetch
    controlU=arm.Control()          
    controlU.insRead(inReg.opcode)  #Set control bit values
    PC=NPC
#    ExecCalc=arm.ALU(
    #Instruction Deconstruction Occurs in IR constructor function

