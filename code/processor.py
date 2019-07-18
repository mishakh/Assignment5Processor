#Assignment 5 ARM Processor
#Classes Needed: 

#Load Instruction Set from file
f = open("assignment5.txt", 'r')
instrucMem = f.readlines()
#for i in range(0,len(instrucMem)):
#    print(instrucMem[i])
for instruc in instrucMem:
    instruc.replace(",","")
    instruc=instruc.split()
    print(instruc)
    

