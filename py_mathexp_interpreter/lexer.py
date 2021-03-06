import enum
import string

class TokenType(enum.Enum):
    NUMBER = "NUMBER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    LPAR = "LPAR"
    RPAR = "RPAR"
    POW = "POW"
    FUNCTION = "FUNCTION"
    CONSTANT = "CONSTANT"

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token: {self.type} : {self.value}"

    def __repr__(self):
        return self.__str__()

class LexerError(Exception):
    pass

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current = self.text[self.pos]

    def step(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current = self.text[self.pos]
        else:
            self.current = None

        return self.current

    def get_num(self):
        number = self.current
        while (char:=self.step()) is not None and char.isdigit():
            number += char

        if char != '.':
            return int(number, 10)

        number += '.'

        while (char:=self.step()) is not None and char.isdigit():
            number += char

        return float(number)

    def get_ascii(self):
        stri = self.current

        while (char:=self.step()) is not None and char in string.ascii_letters:
            stri += char
        return stri


    def ignore_whitespace(self):
        while (self.current is not None) and self.current.isspace():
            self.step()

    def get_next_token(self):
        while (self.current is not None):
            self.ignore_whitespace()

            if self.current.isdigit():
                return Token(TokenType.NUMBER, self.get_num())
            
            if self.current == '+':
                self.step()
                return Token(TokenType.PLUS, '+')
            
            if self.current == '-':
                self.step()
                return Token(TokenType.MINUS, '-')
            
            if self.current == '*':
                self.step()
                return Token(TokenType.MUL, '*')

            if self.current == '/':
                self.step()
                return Token(TokenType.DIV, '/')

            if self.current == '(':
                self.step()
                return Token(TokenType.LPAR, '(')

            if self.current == ')':
                self.step()
                return Token(TokenType.RPAR, ')')

            if self.current == '^':
                self.step()
                return Token(TokenType.POW, '^')

            if self.current == '.':
                self.step()
                return Token(TokenType.DOT, '.')

            if self.current in string.ascii_uppercase:
                return Token(TokenType.FUNCTION, self.get_ascii())

            if self.current in string.ascii_letters:
                return Token(TokenType.CONSTANT, self.get_ascii())

            raise LexerError(f"Unknow token \"{self.current}\" at pos {self.pos}")

        return None