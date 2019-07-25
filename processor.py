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
    reg.regMem()
    inReg=arm.InstructionReg(instrucMem[PC])   #Instruction Fetch
    controlU=arm.Control()          
    controlU.insRead(inReg.opcode)  #Set control bit values
    reg.readRegs(inReg.Rn, inReg.Rm)
    if(controlU.ALUSrc==1):
        if((controlU.memRead==1) or (controlU.memWrite==1)):
            ALU=arm.ALU((inReg.Rn*8), inReg.Imm, controlU.ALUop1, controlU.ALUop2)
        else:
           ALU=arm.ALU(reg.readData1, inReg.Imm, controlU.ALUop1, controlU.ALUop2)
           
    elif(controlU.ALUSrc==0):
        ALU=arm.ALU(reg.readData1, reg.readData2, controlU.ALUop1, controlU.ALUop2)

    ALU.exec(ALU.ALU_c)

    if(controlU.memToReg==0):
        reg.regWrite(inReg.Rd,ALU.output)
    elif(controlU.memToReg==1):
        if(controlU.memRead==1): #LOAD
            reg.regWrite(inReg.Rd, reg.dataMem[ALU.output])
        elif(controlU.memWrite==1): #STORE
                    
    PC=NPC

    #Instruction Deconstruction Occurs in IR constructor function
    
