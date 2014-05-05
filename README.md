pytest-eradicate
===============================================================

[Pytest](http://pytest.org/) plugin for detecting commented out code in python files.

Usage
---------

install via::

    pip install pytest-eradicate

if you then type::

    py.test --eradicade
    
every file ending in ``.py`` will be discovered and checked
for commented out code.

Eradicate
---------

Eradicate is a tool to detect commented out code in Python files.

[Eradicate Github](https://github.com/myint/eradicate)

As the developer states commented out code has no place in your repository.

Besides that, commented out code is often an indicator for debug statements left behind or
code moved out of the way during development.
