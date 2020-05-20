import re
from enum import Enum
import coding
from collections import defaultdict
label_finder = re.compile('(?<=\[)[A-Z][0-9]+(?=\])')
if_finder = re.compile('IF\s+[A-Z][0-9]?\s*!=\s*0\s+GOTO\s+[A-Z][0-9]?')


class i_type(Enum):
    TRIV = 0
    INC = 1
    DEC = 2
    GOTO = 3

def get_instruction_type_var_and_label(inst_string):
    label = None
    instruction_type = None
    var = None
    goto_label = None
    
    if inst_string.startswith('['):
        label = get_label(inst_string)
        inst_string = inst_string[inst_string.find(']')+1:].strip()
    if if_finder.search(inst_string):
        goto_label = get_jump_label_from_if(inst_string)
        var = inst_string.split('!=')[0][3:].strip()
        instruction_type = i_type.GOTO
    else:
        no_spaces = inst_string.replace(' ','')
        var = no_spaces.split('<-')[0]
        default_str = var + "<-" + var
        if re.search(default_str + "\+1", no_spaces):
            instruction_type = i_type.INC
        elif re.search(default_str + "-1", no_spaces):
            instruction_type = i_type.DEC
        elif re.search(default_str, no_spaces):
            instruction_type = i_type.TRIV
    return label, var, instruction_type, goto_label

def get_label(inst_string):
    label = label_finder.search(inst_string)
    if label:
        return label.group(0)

def get_jump_label_from_if(if_string):
    return if_string.split('GOTO')[-1].strip()
        

def encode_file(path_to_encode):
    f = open(path_to_encode, 'r')
    instructions = ''.join([line for line in f.readlines() if line != "\n"])
    return encode_str(instructions)

def encode_str(inst_str):
    instructions = [line.upper() for line in inst_str.split('\n') if line.strip()]
    inst_values = [get_instruction_type_var_and_label(inst) for inst in instructions]
    num_of_X = max({int(tup[1][1:]) for tup in inst_values if tup[1].startswith("X")}.union({0}))
    num_of_Z = max({int(tup[1][1:]) for tup in inst_values if tup[1].startswith("Z")}.union({0}))
    longer = max(num_of_X, num_of_Z)
    X_list = ["X"+str(i+1) for i in range(longer)]
    Z_list = ["Z"+str(i+1) for i in range(longer)]
    variables = ["Y"] + [unit for pair in zip(X_list,Z_list) for unit in pair]
    labels = sorted({tup[0] for tup in inst_values if tup[0]})
    variables = {var:i for i,var in enumerate(variables)}
    labels = {var:i for i,var in enumerate(labels, start = 1)}
    labels[None] = 0
    labels = defaultdict(lambda:len(labels), labels)

    codes = []
    for label, var, inst_type, goto_label in inst_values:
        a = labels[label]
        b = inst_type.value
        c = variables[var]
        if b == 3:
            b = 2 + labels[goto_label]
        inner_encoding = coding.pair_encode(b,c)
        outer_encoding = coding.pair_encode(a,inner_encoding)
        codes.append(outer_encoding)
    program_code = coding.list_encode(*codes)-1
    
    print("Program Instructions:",'\n'.join(instructions), sep="\n")
    print("Program Encoded:", program_code)
    return program_code
    
    

    
    
    





    
