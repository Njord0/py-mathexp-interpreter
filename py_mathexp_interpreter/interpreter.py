from .lexer import Lexer, TokenType
from .parser import Parser, Operand, Operator, Function, UnaryOp
import math


funcs = {
    "sqrt": lambda x: math.sqrt(x)
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

    elif isinstance(node, UnaryOp):
        if node.type == TokenType.MINUS:
            return visit_node(node.node) * (-1)
        elif node.type == TokenType.PLUS:
            return visit_node(node.node)


class InterpreterException(Exception):
    pass

class Interpreter:
    def __init__(self, text: str):
        self._lexer = Lexer(text)
        self.parser = Parser(self._lexer)

        self.ast = self.parser.parse()

    def interpret(self):
        return visit_node(self.ast.root)


