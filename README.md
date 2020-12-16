# py-mathexp-interpreter
> py-mathexp-interpreter is a python library for evaluating mathematical expressions.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python version](https://img.shields.io/badge/python-3.8-green.svg)](https://shields.io/)

py-mathexp-interpreter is a python library for evaluation of mathematical expressions. You can use it to safely interpret arithmetical expressions for you bot for example. It needs python > 3.8 to run properly.
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

from py_mathexp-interpreter import Interpreter

interpreter = Interpreter("(10*10)^2")
print(interpreter.interpret())
```
Result : 10000

You can also use functions inside expressions : 
```python
from py_mathexp-interpreter import Interpreter

interpreter = Interpreter("sqrt(10*10)") # note: function argument can be a complex expression
print(interpreter.interpret())
```
Result: 10.0

You can add your own function ! 
```python
from py-mathexp-interpreter import Interpreter, funcs

funcs["incbyone"] = lambda x: x+1
interpreter = Interpreter("incbyone(3*2)")
print(interpreter.interpret())
```
Result: 7

## Development status

For now, unary operators are not supported ("-1 * 10" expression is not valid)
I plan to add support for constant soon.

## Documentation
Coming soon :(

### Release history
```
v0.0.1  
------
* WIP
```

