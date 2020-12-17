from .interpreter import funcs, constants

class InvalidNameException(Exception):
    pass

def add_constant(name: str, value):
    if (isinstance(value, float) or isinstance(value, int)) and isinstance(name, str):
        if name.islower():
            constants[name] = value
        else:
            raise InvalidNameException("Constant name must be lowercase")

def add_function(name: str, func):
    if (isinstance(name, str)) and isinstance(func, type(lambda:0)):
        if name[0].isupper():
            funcs[name] = func
        else:
            raise InvalidNameException("Function name must start with Uppercase letter.")
