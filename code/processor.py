#Assignment 5 ARM Processor
import processor_c as arm

####INITIAL
#load Instruction Memory
f = open("assignment5.txt", 'r')
instrucMem = f.readlines()
PC=0
reg=arm.Registers()

####RUN TIME
while(PC<len(instrucMem)):
    NPC=PC+1
    
    inReg=arm.InstructionReg(instrucMem[PC])   #Instruction Fetch
    controlU=arm.Control()          
    controlU.insRead(inReg.opcode)  #Set control bit values
    reg.readRegs(inReg.Rn, inReg.Rm)
    if(controlU.ALUSrc==1):
        ALU=arm.ALU(reg.readData1, inReg.Imm, controlU.ALUop1, controlU.ALUop2)
    elif(controlU.ALUSrc==0):
        ALU=arm.ALU(reg.readData1, reg.readData2, controlU.ALUop1, controlU.ALUop2)
    ALU.exec(ALU.ALU_c)
    reg.regWrite(ALU.output,inReg.Rd)
    PC=NPC

    #Instruction Deconstruction Occurs in IR constructor function
    
