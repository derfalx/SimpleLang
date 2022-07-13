from simplelang.instruction import *
from simplelang.machine import StackMachine

code = [Let('foo', Type.NUM, 1), PushVar('foo'), PushVar('foo'), Add(), Print(), PushNum(2), Mul(), Print(), PushNum(4), Equals(), Print()]
machine = StackMachine(code)
machine.execute()


