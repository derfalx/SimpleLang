# Generated from C:/Users/falx/PycharmProjects/SimpleLang\SimpleLang.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,4,0,13,
        8,0,11,0,12,0,14,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,32,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,40,8,2,10,
        2,12,2,43,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,1,3,1,3,1,3,
        5,3,73,8,3,10,3,12,3,76,9,3,1,4,1,4,1,4,0,2,4,6,5,0,2,4,6,8,0,5,
        1,0,3,4,1,0,1,2,1,0,13,14,1,0,15,16,1,0,11,12,88,0,12,1,0,0,0,2,
        22,1,0,0,0,4,31,1,0,0,0,6,64,1,0,0,0,8,77,1,0,0,0,10,13,3,8,4,0,
        11,13,3,2,1,0,12,10,1,0,0,0,12,11,1,0,0,0,13,14,1,0,0,0,14,12,1,
        0,0,0,14,15,1,0,0,0,15,1,1,0,0,0,16,17,3,4,2,0,17,18,5,19,0,0,18,
        23,1,0,0,0,19,20,3,6,3,0,20,21,5,19,0,0,21,23,1,0,0,0,22,16,1,0,
        0,0,22,19,1,0,0,0,23,3,1,0,0,0,24,25,6,2,-1,0,25,26,5,5,0,0,26,27,
        3,4,2,0,27,28,5,6,0,0,28,32,1,0,0,0,29,32,5,20,0,0,30,32,5,21,0,
        0,31,24,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,41,1,0,0,0,33,34,
        10,4,0,0,34,35,7,0,0,0,35,40,3,4,2,5,36,37,10,3,0,0,37,38,7,1,0,
        0,38,40,3,4,2,4,39,33,1,0,0,0,39,36,1,0,0,0,40,43,1,0,0,0,41,39,
        1,0,0,0,41,42,1,0,0,0,42,5,1,0,0,0,43,41,1,0,0,0,44,45,6,3,-1,0,
        45,46,5,5,0,0,46,47,3,6,3,0,47,48,5,6,0,0,48,65,1,0,0,0,49,50,5,
        9,0,0,50,65,3,6,3,5,51,52,3,4,2,0,52,53,5,10,0,0,53,54,3,4,2,0,54,
        65,1,0,0,0,55,56,3,4,2,0,56,57,7,2,0,0,57,58,3,4,2,0,58,65,1,0,0,
        0,59,60,3,4,2,0,60,61,7,3,0,0,61,62,3,4,2,0,62,65,1,0,0,0,63,65,
        7,4,0,0,64,44,1,0,0,0,64,49,1,0,0,0,64,51,1,0,0,0,64,55,1,0,0,0,
        64,59,1,0,0,0,64,63,1,0,0,0,65,74,1,0,0,0,66,67,10,7,0,0,67,68,5,
        7,0,0,68,73,3,6,3,8,69,70,10,6,0,0,70,71,5,8,0,0,71,73,3,6,3,7,72,
        66,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,
        0,75,7,1,0,0,0,76,74,1,0,0,0,77,78,5,19,0,0,78,9,1,0,0,0,9,12,14,
        22,31,39,41,64,72,74
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'and'", "'or'", "<INVALID>", "'=='", "'true'", "'false'", 
                     "'<'", "'<='", "'>'", "'>='", "'='", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "ADD", "SUB", "MUL", "DIV", "LP", "RP", 
                      "AND", "OR", "NOT", "EQUALS", "TRUE", "FALSE", "LESS_THAN", 
                      "LESS_EQ_THAN", "GREATER_THAN", "GREATER_EQ_THAN", 
                      "ASSIGN", "ID", "SEMICOLON", "NUMBER", "FLOAT", "WS" ]

    RULE_code = 0
    RULE_expr = 1
    RULE_arithmetic_expr = 2
    RULE_bool_expr = 3
    RULE_statement = 4

    ruleNames =  [ "code", "expr", "arithmetic_expr", "bool_expr", "statement" ]

    EOF = Token.EOF
    ADD=1
    SUB=2
    MUL=3
    DIV=4
    LP=5
    RP=6
    AND=7
    OR=8
    NOT=9
    EQUALS=10
    TRUE=11
    FALSE=12
    LESS_THAN=13
    LESS_EQ_THAN=14
    GREATER_THAN=15
    GREATER_EQ_THAN=16
    ASSIGN=17
    ID=18
    SEMICOLON=19
    NUMBER=20
    FLOAT=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExprContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode" ):
                listener.enterCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode" ):
                listener.exitCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode" ):
                return visitor.visitCode(self)
            else:
                return visitor.visitChildren(self)




    def code(self):

        localctx = SimpleLangParser.CodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_code)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SimpleLangParser.SEMICOLON]:
                    self.state = 10
                    self.statement()
                    pass
                elif token in [SimpleLangParser.LP, SimpleLangParser.NOT, SimpleLangParser.TRUE, SimpleLangParser.FALSE, SimpleLangParser.NUMBER, SimpleLangParser.FLOAT]:
                    self.state = 11
                    self.expr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleLangParser.LP) | (1 << SimpleLangParser.NOT) | (1 << SimpleLangParser.TRUE) | (1 << SimpleLangParser.FALSE) | (1 << SimpleLangParser.SEMICOLON) | (1 << SimpleLangParser.NUMBER) | (1 << SimpleLangParser.FLOAT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic_expr(self):
            return self.getTypedRuleContext(SimpleLangParser.Arithmetic_exprContext,0)


        def SEMICOLON(self):
            return self.getToken(SimpleLangParser.SEMICOLON, 0)

        def bool_expr(self):
            return self.getTypedRuleContext(SimpleLangParser.Bool_exprContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = SimpleLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.arithmetic_expr(0)
                self.state = 17
                self.match(SimpleLangParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.bool_expr(0)
                self.state = 20
                self.match(SimpleLangParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.laexpr = None # Arithmetic_exprContext
            self.op = None # Token
            self.raexprl = None # Arithmetic_exprContext
            self.raexpr = None # Arithmetic_exprContext

        def LP(self):
            return self.getToken(SimpleLangParser.LP, 0)

        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Arithmetic_exprContext,i)


        def RP(self):
            return self.getToken(SimpleLangParser.RP, 0)

        def NUMBER(self):
            return self.getToken(SimpleLangParser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(SimpleLangParser.FLOAT, 0)

        def MUL(self):
            return self.getToken(SimpleLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(SimpleLangParser.DIV, 0)

        def ADD(self):
            return self.getToken(SimpleLangParser.ADD, 0)

        def SUB(self):
            return self.getToken(SimpleLangParser.SUB, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_arithmetic_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_expr" ):
                listener.enterArithmetic_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_expr" ):
                listener.exitArithmetic_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expr" ):
                return visitor.visitArithmetic_expr(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.Arithmetic_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_arithmetic_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleLangParser.LP]:
                self.state = 25
                self.match(SimpleLangParser.LP)
                self.state = 26
                self.arithmetic_expr(0)
                self.state = 27
                self.match(SimpleLangParser.RP)
                pass
            elif token in [SimpleLangParser.NUMBER]:
                self.state = 29
                self.match(SimpleLangParser.NUMBER)
                pass
            elif token in [SimpleLangParser.FLOAT]:
                self.state = 30
                self.match(SimpleLangParser.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.Arithmetic_exprContext(self, _parentctx, _parentState)
                        localctx.laexpr = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleLangParser.MUL or _la==SimpleLangParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        localctx.raexprl = self.arithmetic_expr(5)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.Arithmetic_exprContext(self, _parentctx, _parentState)
                        localctx.laexpr = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SimpleLangParser.ADD or _la==SimpleLangParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        localctx.raexpr = self.arithmetic_expr(4)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Bool_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.lbexpr = None # Bool_exprContext
            self.laexpr = None # Arithmetic_exprContext
            self.raexpr = None # Arithmetic_exprContext
            self.op = None # Token
            self.rbexpr = None # Bool_exprContext

        def LP(self):
            return self.getToken(SimpleLangParser.LP, 0)

        def bool_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Bool_exprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Bool_exprContext,i)


        def RP(self):
            return self.getToken(SimpleLangParser.RP, 0)

        def NOT(self):
            return self.getToken(SimpleLangParser.NOT, 0)

        def EQUALS(self):
            return self.getToken(SimpleLangParser.EQUALS, 0)

        def arithmetic_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Arithmetic_exprContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Arithmetic_exprContext,i)


        def LESS_EQ_THAN(self):
            return self.getToken(SimpleLangParser.LESS_EQ_THAN, 0)

        def LESS_THAN(self):
            return self.getToken(SimpleLangParser.LESS_THAN, 0)

        def GREATER_EQ_THAN(self):
            return self.getToken(SimpleLangParser.GREATER_EQ_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(SimpleLangParser.GREATER_THAN, 0)

        def TRUE(self):
            return self.getToken(SimpleLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SimpleLangParser.FALSE, 0)

        def AND(self):
            return self.getToken(SimpleLangParser.AND, 0)

        def OR(self):
            return self.getToken(SimpleLangParser.OR, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_bool_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr" ):
                listener.enterBool_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr" ):
                listener.exitBool_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr" ):
                return visitor.visitBool_expr(self)
            else:
                return visitor.visitChildren(self)



    def bool_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.Bool_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_bool_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 45
                self.match(SimpleLangParser.LP)
                self.state = 46
                self.bool_expr(0)
                self.state = 47
                self.match(SimpleLangParser.RP)
                pass

            elif la_ == 2:
                self.state = 49
                self.match(SimpleLangParser.NOT)
                self.state = 50
                self.bool_expr(5)
                pass

            elif la_ == 3:
                self.state = 51
                localctx.laexpr = self.arithmetic_expr(0)
                self.state = 52
                self.match(SimpleLangParser.EQUALS)
                self.state = 53
                localctx.raexpr = self.arithmetic_expr(0)
                pass

            elif la_ == 4:
                self.state = 55
                localctx.laexpr = self.arithmetic_expr(0)
                self.state = 56
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SimpleLangParser.LESS_THAN or _la==SimpleLangParser.LESS_EQ_THAN):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 57
                localctx.raexpr = self.arithmetic_expr(0)
                pass

            elif la_ == 5:
                self.state = 59
                localctx.laexpr = self.arithmetic_expr(0)
                self.state = 60
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SimpleLangParser.GREATER_THAN or _la==SimpleLangParser.GREATER_EQ_THAN):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 61
                localctx.raexpr = self.arithmetic_expr(0)
                pass

            elif la_ == 6:
                self.state = 63
                _la = self._input.LA(1)
                if not(_la==SimpleLangParser.TRUE or _la==SimpleLangParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.Bool_exprContext(self, _parentctx, _parentState)
                        localctx.lbexpr = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 67
                        self.match(SimpleLangParser.AND)
                        self.state = 68
                        localctx.rbexpr = self.bool_expr(8)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.Bool_exprContext(self, _parentctx, _parentState)
                        localctx.lbexpr = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_bool_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 70
                        self.match(SimpleLangParser.OR)
                        self.state = 71
                        localctx.rbexpr = self.bool_expr(7)
                        pass

             
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(SimpleLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SimpleLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.arithmetic_expr_sempred
        self._predicates[3] = self.bool_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_expr_sempred(self, localctx:Arithmetic_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def bool_expr_sempred(self, localctx:Bool_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




