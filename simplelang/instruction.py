from enum import Enum


class OpCode(Enum):
    PUSH_NUM = 0x001
    PUSH_BOOL = 0x002
    POP = 0x003
    PUSH_VAR = 0x004
    POP_VAR = 0x005

    ADD = 0x011
    SUB = 0x012
    MUL = 0x013
    DIV = 0x014

    AND = 0x021
    OR = 0x022
    EQUALS = 0x023
    LESS_THAN = 0x024
    LESS_EQ_THAN = 0x025
    GREATER_THAN = 0x026
    GREATER_EQ_THAN = 0x027

    PRINT = 0x031
    LET = 0x032
    ASSIGN = 0x033


class Type(Enum):
    NUM = 'Number'
    FLOAT = 'Float'
    BOOL = 'Bool'


class Instruction:
    def __init__(self, opcode: OpCode):
        self.opcode = opcode


class PushNum(Instruction):
    def __init__(self, num: int | float):
        super().__init__(OpCode.PUSH_NUM)
        self.num = num


class PushBool(Instruction):
    def __init__(self, bval: bool):
        super().__init__(OpCode.PUSH_BOOL)
        super.bool = bval


class Pop(Instruction):
    def __init__(self):
        super().__init__(OpCode.POP)


class Add(Instruction):
    def __init__(self):
        super().__init__(OpCode.ADD)


class Sub(Instruction):
    def __init__(self):
        super().__init__(OpCode.SUB)


class Mul(Instruction):
    def __init__(self):
        super().__init__(OpCode.MUL)


class Div(Instruction):
    def __init__(self):
        super().__init__(OpCode.DIV)


class Print(Instruction):
    def __init__(self):
        super().__init__(OpCode.PRINT)


class And(Instruction):
    def __init__(self):
        super().__init__(OpCode.AND)


class Or(Instruction):
    def __init__(self):
        super().__init__(OpCode.OR)


class Equals(Instruction):
    def __init__(self):
        super().__init__(OpCode.EQUALS)


class LessThan(Instruction):
    def __init__(self):
        super().__init__(OpCode.LESS_THAN)


class LessEqualThan(Instruction):
    def __init__(self):
        super().__init__(OpCode.LESS_EQ_THAN)


class GreaterThan(Instruction):
    def __init__(self):
        super().__init__(OpCode.GREATER_THAN)


class GreaterEqualThan(Instruction):
    def __init__(self):
        super().__init__(OpCode.GREATER_EQ_THAN)


class Let(Instruction):
    def __init__(self, var_name: str, var_type: Type, init_val: (bool | float | int)):
        super().__init__(OpCode.LET)
        self.var_name = var_name
        self.var_type = var_type
        self.init_val = init_val


class PushVar(Instruction):
    def __init__(self, var_name: str):
        super().__init__(OpCode.PUSH_VAR)
        self.var_name = var_name


class PopVar(Instruction):
    def __init__(self, var_name: str):
        super().__init__(OpCode.POP_VAR)
        self.var_name = var_name
