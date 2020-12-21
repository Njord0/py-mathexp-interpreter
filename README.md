# py-mathexp-interpreter
> py-mathexp-interpreter is a python library for evaluating mathematical expressions.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python version](https://img.shields.io/badge/python-3.8-green.svg)](https://shields.io/)

py-mathexp-interpreter is a python library for evaluation of mathematical expressions. You can use it to safely interpret arithmetical expressions for your bot for example. It needs python > 3.8 to run properly.
No dependencies are needed except python standard library. 

## Installation
From github:
```sh
git clone https://github.com/njord0/py-mathexp-interpreter
cd py-mathexp-interpreter
python3 setup.py install
```

from Pypi:
```sh
TODO
```

## Usage example

```python

from py_mathexp_interpreter import Interpreter

interpreter = Interpreter()
print(interpreter.interpret("(10*10)^2"))
```
Result : 10000

You can also use functions inside expressions : 
```python
from py_mathexp_interpreter import Interpreter

interpreter = Interpreter() 
print(interpreter.interpret("Sqrt(10*10)")) # note: function argument can be a complex expression
```
Result: 10.0

You can add your own function and constant ! 
```python
from py_mathexp_interpreter import Interpreter, add_function, add_constant

add_function("Incbyone", lambda x: x+1)
add_constant("three", 3)

interpreter = Interpreter()
print(interpreter.interpret("Incbyone(three*2)"))
```
Result: 7

## Development status

Unary operators and constants are now suppported !

## Documentation
Coming soon :(

### Release history
```
v0.0.2 (17/12/2020)
------
* Added support for unary operators
* Added support for constant
* Improved way to add new functions and constants
* Added new file (utils.py)
* Functions name must now start with a capital letter
* Improved interpreter (so you don't have to instantiate a new Interpreter object each time.)

v0.0.1  
------
* WIP
```

