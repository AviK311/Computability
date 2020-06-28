import re
import coding
from collections import defaultdict
label_order = "ABCDE"

label_finder = re.compile('(?<=\[)[A-E][0-9]+(?=\])')
if_finder = re.compile('(?<=IF)(?:\s*)((?:X|Y|Z)[0-9])(?:\s*!=\s*0\s+GOTO\s+)([A-E][1-9]*)')
var_finder = re.compile('(X|Z|Y)[0-9]*(?=\s*<-)')


def encode_instruction(inst_string):
    inst_type = 0
    label_num = 0
    label = get_label(inst_string)
    if label:
        label_num = 1 + label_order.index(label[0]) + (int(label[1:]) - 1)*5
    if_inst = if_finder.search(inst_string)
    if if_inst:
        var = if_inst.group(1)
        jump_label = if_inst.group(2)
        inst_type = 3 + label_order.index(jump_label[0]) + (int(jump_label[1:]) - 1)*5
    else:
        var = var_finder.search(inst_string).group(0)
        if '+' in inst_string:
            inst_type = 1
        elif inst_string.count('-') == 2:
            inst_type = 2
    if var == 'Y':
        var_num = 0
    elif var.startswith('X'):
        var_num = int(var[1:])*2 - 1
    else:
        var_num = int(var[1:])*2
    return label_num, inst_type, var_num
        
    
    



def get_label(inst_string):
    label = label_finder.search(inst_string)
    if label:
        return label.group(0)
    else:
        return None



def encode_file(path_to_encode):
    f = open(path_to_encode, 'r')
    instructions = ''.join([line for line in f.readlines() if line != "\n"])
    return encode_str(instructions)



def encode_str(inst_str):
    instructions = [line.upper() for line in inst_str.split('\n') if line.strip()]
    encoded_instructions = [encode_instruction(inst) for inst in instructions]
    encoded_instructions = [coding.pair_encode(a, coding.pair_encode(b,c)) for a,b,c in encoded_instructions]
    
    program_code = coding.list_encode(*encoded_instructions)-1
    
    print("Program Instructions:",'\n'.join(instructions), sep="\n")
    print("Program Encoded:", program_code)
    return program_code
    
    

    
    
    





    
