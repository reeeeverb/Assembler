def split_r_code(inst):
    inst = bin(inst)[2:].zfill(32)
    op = inst[:6]
    rs = int(inst[6:11],2)
    rt = int(inst[11:16],2)
    rd = int(inst[16:21],2)
    shamt = int(inst[21:26],2) # shift amount
    funct = int(inst[26:],2)
    print(op,rs,rt,rd,shamt,funct)

def split_i_code(inst):
    inst = bin(inst)[2:].zfill(32)
    op = inst[:6]
    rs = int(inst[6:11],2)
    rt = int(inst[11:16],2)
    imm = int(inst[16:],2)
    print(op,rs,rt,imm)

x = int(input(),16)
print(split_i_code(x))
