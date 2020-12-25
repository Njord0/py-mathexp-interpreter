from .lexer import Lexer, TokenType, Token

class AST:
    def __init__(self, root_node):
        self.root = root_node

class Node:
    def __init__(self, _type, value, left_node, right_node):
        self.type = _type
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        return f"type: {self.type}, value: {self.value}"

    def __repr__(self):
        return self.__str__()

class Operand(Node):
    def __init__(self, _type, value):
        self.type = _type
        self.value = value

class Operator(Node):
    def __init__(self, _type, value, left_node, right_node):
        super().__init__(_type, value, left_node, right_node)


class Function(Node):
    def __init__(self, _type, value, args=[None]):
        self.type = _type
        self.value = value
        self.args = args

class UnaryOp(Node):
    def __init__(self, _type, value, node):
        self.type = _type
        self.value = value
        self.node = node

class OperandConstant(Node):
    def __init__(self, _type, value):
        self.type = _type
        self.value = value # constant_name


class ParserException(Exception):
    pass
 
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def check(self, token_type):
        if self.current_token != None and self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ParserException("Syntax error.")

    def factor(self):

        while self.current_token != None:
            token = self.current_token

            if token.type == TokenType.MINUS:
                self.check(TokenType.MINUS)
                node = UnaryOp(token.type, token.value, self.factor())

            elif token.type == TokenType.PLUS:
                self.check(TokenType.PLUS)
                node = UnaryOp(token.type, token.value, self.factor())

            elif self.current_token.type == TokenType.FUNCTION:
                self.check(TokenType.FUNCTION)
                self.check(TokenType.LPAR)
                node = Function(token.type, token.value, self.expr())
                self.check(TokenType.RPAR)

            elif self.current_token.type == TokenType.CONSTANT:
                self.check(TokenType.CONSTANT)
                node = OperandConstant(token.type, token.value)

            elif self.current_token.type == TokenType.LPAR:
                self.check(TokenType.LPAR)
                node = self.expr()
                self.check(TokenType.RPAR)

            elif self.current_token.type == TokenType.NUMBER:
                self.check(TokenType.NUMBER)
                node = Operand(token.type, token.value)




            else:
                raise ParserException("Can't have two operators consecutively")

            if self.current_token != None and self.current_token.type == TokenType.POW:
                self.check(TokenType.POW)
                node = Operator(TokenType.POW, token.value, self.expr(), node)
                
            return node

    def term(self):

        node = self.factor()

        while self.current_token != None and self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token
            if token.type == TokenType.MUL:
                self.check(TokenType.MUL)
            elif token.type == TokenType.DIV:
                self.check(TokenType.DIV)

            if (factor:=self.factor()) == None:
                raise ParserException("Mul|div operator needs two operands")        
      
            node = Operator(token.type, token.value, factor, node)
        
        return node


    def expr(self):

        node = self.term()

        while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token

            if self.current_token.type == TokenType.PLUS:
                self.check(TokenType.PLUS)

            elif self.current_token.type == TokenType.MINUS:
                self.check(TokenType.MINUS)

            if (term:=self.term()) == None:
                raise ParserException("Plus|minus operator needs two operands")
            node = Operator(token.type, token.value, term, node)

        return node


    def parse(self):
        return AST(self.expr())
