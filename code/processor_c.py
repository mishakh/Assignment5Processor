
class Registers:
    def __init__(self):
        self.X=[0]*32
        self.dataMem=[0]*32
        readData1 = 0
        readData2 = 0
    def regWrite(self, wReg, wData):
        self.X[wReg]=wData

    def readRegs(self, rReg1, rReg2):
        self.readData1=self.X[rReg1]
        self.readData2=self.X[rReg2]
 #       print(self.readData1, self.readData2)
        
        
class Control:

    def __init__(self):
        self.reg2Loc = 0
        self.branch = 0
        self.memRead = 0
        self.memToReg = 0
        self.ALUop1 = 0
        self.ALUop2 = 0
        self.memWrite = 0
        self.ALUSrc = 0
        self.regWrite = 0
        self.uncond = 0
        

    def insRead(self, opcode):
        #reads opcode and sets control bit values
        if(opcode==('ADD') or opcode==('SUB') or opcode==('AND') or opcode==('ORR')):
            self.regWrite = 1
            self.ALUop1 = 1
        
        elif(opcode==('LDUR') or opcode==('STUR')):
            self.ALUSrc = 1
            self.memToReg = 1
            self.regWrite = 1
            if opcode==('LDUR'):
                self.memRead = 1
            elif opcode==('STUR'):
                self.memWrite = 1
                
        elif(opcode==('ADDI') or opcode==('SUBI')):
            self.regWrite = 1
            self.ALUop1 = 1
            self.ALUSrc = 1

        elif(opcode==('CBZ') or opcode==('B')):
            self.branch = 1
            self.ALUSrc = 1
            if(opcode=='B'):
                self.uncond = 1
        print('                     ',self.reg2Loc, self.branch, self.memRead, self.memToReg, self.ALUop1, self.ALUop2, self.memWrite,
             self.ALUSrc, self.regWrite, self.uncond,'\n')
            
class InstructionReg:
    opcode=0
    Rd=0
    Rn=0
    Rm=0
    Imm=0
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
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])     # R-Format 
            self.Rm=int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.Rm)
        elif (self.opcode=='LDUR' or self.opcode=='STUR'):
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])     # D-Format
            self.Imm= int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.Imm)
        elif(self.opcode=='ADDI' or self.opcode=='SUBI'):
            self.Rd=int(instruc[1])
            self.Rn=int(instruc[2])     # I-Format
            self.Imm=int(instruc[3])
            print(self.opcode,self.Rd,self.Rn,self.Imm)
        elif(self.opcode=='B' or self.opcode=='CBZ'):
            self.addr=int(instruc[1])
            if(self.opcode=='CBZ'):     # B-Format 
                self.Rd=int(instruc[1])
                self.addr=int(instruc[2])
            print(self.opcode, self.Rd, self.addr)
class ALU:

    def __init__(self,in1,in2,ALU_op1,ALU_op2):
        self.in1 = in1
        self.in2 = in2
        self.ALU_op=str(ALU_op1)+str(ALU_op2)
        self.ALU_c=0
        self.output = 0
        self.zero = 0
        
    def ALUcontrol(self, ALUop, opcode):
        if(ALUop == '00'):
            #LDUR AND STUR operations
            self.ALU_c = 0 #add
        if (ALUop == '01'):
            #CBZ
            self.ALU_c = 2 #pass b
        
        if (ALUop == '10'):
            if((opcode=='ADD') or (opcode=='ADDI')):
                self.ALU_c = 0 #add
            elif((opcode=='SUB') or (opcode=='SUBI')):
                self.ALU_c = 1 #sub
            elif(opcode=='AND'):
                self.ALU_c = 3 #AND
            elif(opcode=='ORR'):
                self.ALU_c = 4 #ORR
            
            
    # This will execute whatever operation called at the method
    def exec(self, control):
        control=self.ALU_c
        if(control==0):
            self.output=self.in1+self.in2
        if(control==1):
            self.output=self.in1-self.in2
        if(control==2):
            self.output=self.in1
        print(self.output)
            
