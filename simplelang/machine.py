from dataclasses import dataclass
from typing import List

from simplelang.instruction import *


@dataclass
class Var:
    var_type: Type
    var_value: (bool | int | float)


class StackMachine:
    def __init__(self, code: List[Instruction]):
        self.code = code
        self.stack = list()
        self.pc = -1
        self.pop = None
        self.memory = dict()

    def execute(self):
        self.pc = 0
        while 0 <= self.pc < len(self.code):
            instruction = self.code[self.pc]
            match instruction:
                case PushNum(num=num):
                    self.stack.append(num)
                case PushBool(bval=bval):
                    self.stack.append(bval)
                case Pop():
                    self.pop = self.stack.pop()
                case Add():
                    self._binary_op(lambda x, y: x + y)
                case Sub():
                    self._binary_op(lambda x, y: x - y)
                case Mul():
                    self._binary_op(lambda x, y: x * y)
                case Div():
                    self._binary_op(lambda x, y: x / y)
                case Print():
                    print(self.stack[-1])
                case And():
                    self._binary_op(lambda x, y: x and y)
                case Or():
                    self._binary_op(lambda x, y: x or y)
                case Equals():
                    self._binary_op(lambda x, y: x == y)
                case GreaterThan():
                    self._binary_op(lambda x, y: x > y)
                case GreaterEqualThan():
                    self._binary_op(lambda x, y: x >= y)
                case LessThan():
                    self._binary_op(lambda x, y: x < y)
                case LessEqualThan():
                    self._binary_op(lambda x, y: x <= y)
                case Let(var_name=var_name, var_type=var_type, init_val=init_val):
                    if var_name in self.memory:
                        raise RuntimeError(f"Redefining existing var={var_name}")
                    self.memory[var_name] = Var(var_type, init_val)
                case PushVar(var_name=var_name):
                    if var_name not in self.memory:
                        raise RuntimeError(f"Trying to access non-existent var={var_name}")
                    var = self.memory[var_name]
                    self.stack.append(var.var_value)
                case PopVar(var_name=var_name):
                    if var_name not in self.memory:
                        raise RuntimeError(f"Trying to access non-existent var={var_name}")
                    var = self.memory[var_name]
                    new_val = self.stack.pop()
                    var.var_value = new_val

            self.pc += 1

    def _binary_op(self, operation):
        r_val = self.stack.pop()
        l_val = self.stack.pop()
        self.stack.append(operation(l_val, r_val))



