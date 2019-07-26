#Assignment 5 ARM Processor
import processor_c as arm

####INITIAL
#load Instruction Memory
f = open("assignment5.txt", 'r')
instrucMem = f.readlines()
PC=0
reg=arm.Registers()     #create register object with Registers and Data Memory
reg.dataMem[0]=10      
reg.dataMem[1]=13       #load in data memory array values

####RUN TIME
while(PC<len(instrucMem)):   
        NPC=PC+1        #calculate New Program Counter
        inReg=arm.InstructionReg(instrucMem[PC])   #Instruction Fetch
#Instruction Deconstruction Occurs in IR constructor function

        controlU=arm.Control()  #creates control unit for this instruction (with all flags set low)
        controlU.insRead(inReg.opcode)  #Set control bit values

        reg.readRegs(inReg.Rn, inReg.Rm) #read in values from Rn and Rm registers
        if(controlU.branch==1):
                ALU=arm.ALU(reg.X[inReg.Rd],inReg.Imm,controlU.ALUop1,controlU.ALUop2)
                                        #creates ALU operation for B type instructions
        elif(controlU.ALUSrc==1):
                ALU=arm.ALU(reg.readData1, inReg.Imm, controlU.ALUop1, controlU.ALUop2)
                                        #creates ALU operation for I type and D type instructions
        elif(controlU.ALUSrc==0):
                ALU=arm.ALU(reg.readData1, reg.readData2, controlU.ALUop1, controlU.ALUop2)
                                        #creates ALU operation for R type instructions
        ALU.ALUcontrol(ALU.ALU_op,inReg.opcode)
                                        #read in ALU op and set the appropriate ALU operation
        ALU.exec(ALU.ALU_c)     #perform ALU operation, place result in ALU.output

        if((controlU.memToReg==0) and (controlU.branch==0)):
                reg.regWrite(inReg.Rd,ALU.output)       #write back for R type instructions
                PC=NPC
        elif(controlU.memToReg==1):
                if(controlU.memRead==1): #LOAD
                        reg.regWrite(inReg.Rd, reg.dataMem[ALU.output])  #load data memory value to Rd                      
                        print('Data Memory:\n',reg.dataMem)
                elif(controlU.memWrite==1): #STORE
                        reg.dataMem[ALU.output]=reg.X[inReg.Rd] #load Rd value to calculated Data Memory Address
                        print('Data Memory:\n',reg.dataMem)

                PC=NPC #go to next sequential instrution
                
        elif(controlU.branch==1):  #Check for branch opcode
                if(controlU.uncond==1):  # B instruction
                        PC= PC+inReg.Imm  #PC <- PC+addr
                        print("PC: "+str(PC))
                        print('-----------------------\n')
                        continue
                elif(ALU.zero==1):  #if R[Rd]==0
                        PC = PC+inReg.Imm  #PC <- PC+addr
                        print('Registers:\n',(reg.X))
                        print("PC: "+str(PC))
                        print('-----------------------\n')
                        continue
                else:
                        print('Registers:\n',(reg.X))
                        print("PC: "+str(PC)) #if CBZ result is false, continue sequentially
                        PC=NPC
        print('Registers:\n',(reg.X))
        print("PC: "+str(PC))
        print('-----------------------\n')
print('END OF FILE')                        

       
