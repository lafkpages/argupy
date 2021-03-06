# argupy
Easy-to-use argument manager for Python3.

## Instalation
To install argupy, run
``` bash
pip3 install argupy
```

## Usage
To use it in a Python script, first you need to import it.
``` python
from argupy import *
```

Then, initialize the `Args` class
``` python
argupy = Args()
```
and define any parameters you'll want to use later on.
``` python
argupy.setarg('--testarg', BOOL)
```
You can optionally pass a list of parameters to `Args()`, but if you don't, it defaults to `sys.argv`. The first item will be ignored.

The `setarg` function takes these parameters:
* **name**: the parameter name, for example, '--test'.
* **type_**: the parameter type, pass a constant like `BOOL`, `STR`, `INT`, or `FLOAT`. Note the underscore to prevent conflicts with the built-in `type()` function.
* **default_value**: *optional*. The default value to return if the argument is not present. Defaults to `False` if the argument is of type `BOOL`.
* **short**: *optional*. The short name for the argument, usually one letter. For example, long: `--help`, short: `-h`.

To use short names, do it like this:
``` python
argupy.setarg('--testarg', BOOL, short='-t')
```

To define an argument which takes a value, use the types `STR`, `INT` or `FLOAT`. Then retreive it with the `Args.arg()` method.
``` python
argupy.setarg('--testarg', STR)

value = argupy.arg('--testarg')

print(type(value), value)
# Running this code like this: 
# python3 file.py --testarg hello
# would output: <class 'str'> hello
```

If the argument type is set to `STR`, the returned value will be of type `str`. And again, if the argument is of type `INT` or `FLOAT`, the returned value will be of type `int` or `float`, so you don't have to pass it through `int()` or `float()`. Unless the argument is not present and the default value you specify is not of the corresponding type.
To pass `STR` values with spaces, put double-quotes around them, like this:
``` bash
python3 file.py --testarg "Chicago, Los Angeles"
```

Also, for debugging purposes, if you print an argument like this
``` python
print(argupy.args['--testarg'])
```
the output will be something like:
``` bash
Arg(name='--testarg', type_='boolean', default_value=False)
```
or
``` bash
Arg(name='--testarg', type_='boolean', default_value=False, link=True, target='--anotherarg')
```
or
``` bash
Arg(name='--testarg', type_='boolean', default_value=False, links=['--anotherarg'])
```