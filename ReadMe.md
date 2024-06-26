# Py-Decorate-All

Apply a decorator to all functions in a module.

## Installation
```sh
pip install decorate-all
```

## Example Usage

```python
from decorate_all import decorate_all_functions
decorate_all_functions(my_decorator, my_module)
```

decorator (function): the decorator to apply to functions
module_name (string): the name of the module to apply the decorator to

If you want to apply the decorator to functions in the current module, pass `__name__` the module as make sure to call `decorate_all_functions` after defining the functions to decorate, i.e. at the end of the script to apply to all functions.

Here is an example for applying a decorator to all functions in a script:
_(works in a module or interactive console (REPL))_

```python
from decorate_all import decorate_all_functions

def test_function():
    print("Hello there")


def demo_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Decorator was here!"
    
    return wrapper

decorate_all_functions(demo_decorator, __name__)

print(test_function())
```

The output of the above code is:
```
Hello there
Decorator was here!
```
