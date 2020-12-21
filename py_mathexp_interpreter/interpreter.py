from .lexer import Lexer, TokenType
from .parser import Parser, Operand, Operator, Function, UnaryOp, OperandConstant
import math


funcs = {
    "Sqrt": lambda x: math.sqrt(x),
    "Exp": lambda x: math.exp(x),
    "Fact": lambda x: math.factorial(x),
    "Cos": lambda x: math.cos(x),
    "Sin": lambda x: math.sin(x),
    "Tan": lambda x: math.tan(x),
    "Ln": lambda x: math.log(x), #natural logarithm
    "Log": lambda x: math.log10(x) #decimal logarithm

}

constants = {
    "pi": math.pi, 
    "e": math.e
}
def visit_node(node):
    if isinstance(node, Operand):
        return node.value

    elif isinstance(node, Operator):
        if node.type == TokenType.PLUS:
            node = visit_node(node.right_node) + visit_node(node.left_node)
            return node
        elif node.type == TokenType.MINUS:
            node = visit_node(node.right_node) - visit_node(node.left_node)
            return node
        elif node.type == TokenType.MUL:
            node = visit_node(node.right_node) * visit_node(node.left_node)
            return node
        elif node.type == TokenType.DIV:
            node = visit_node(node.right_node) // visit_node(node.left_node)
            return node
        elif node.type == TokenType.POW:
            node = visit_node(node.right_node) ** visit_node(node.left_node)
            return node

    elif isinstance(node, Function):
        val = visit_node(node.args) ## Function.args can be an expression

        try:
            ret = funcs[node.value](val)
        except KeyError:
            raise InterpreterException(f"Function \"{node.value}\" not found")

        return ret

    elif isinstance(node, OperandConstant):
        try:
            val = constants[node.value] #constant_name
        except KeyError:
            raise InterpreterException(f"Constant \"{node.value}\" not found")

        return val

    elif isinstance(node, UnaryOp):
        if node.type == TokenType.MINUS:
            return visit_node(node.node) * (-1)
        elif node.type == TokenType.PLUS:
            return visit_node(node.node)


class InterpreterException(Exception):
    pass

class Interpreter:
    def __init__(self):
        pass

    def interpret(self, text: str):

        self._lexer = Lexer(text.replace(" ", ""))
        self.parser = Parser(self._lexer)

        self.ast = self.parser.parse()

        return visit_node(self.ast.root)


