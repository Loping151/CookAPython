# Step 1

Hello. I am the tour guide for this journey. I will guide you through the steps to create a Python module in C++.

In this section, we will create a simple C++ file that will be used as a Python module.

## Prerequisites
I recommend you use VScode, with Python, C++, Cython extensions installed.

```bash
conda create -n cap python=3.10
conda activate cap

pip install cython # easiest way to use C code.
pip install numpy # frequently used for numerical operations
pip install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu118 # u should change the cuda version according to your system. u should find instructions on the pytorch website.
```
## Step 1.0: Create a directory
Create a directory named `cadd_module` and navigate to it.

## Step 1.1: A simple C++ file
To get started, create a simple file named double_add.h with the following content:

```cpp
#ifndef DOUBLE_ADD_H
#define DOUBLE_ADD_H

double cpp_double_add(double x, double y);

#endif
```

Then create a file named double_add.cpp with the following content:

```cpp
#include "double_add.h"

double cpp_double_add(double x, double y) {
    return x + y;
}

```

I think anyone can read it.

## Step 1.2: Cython definition file
Create a file named double.pyx with the following content:

```python
# distutils: language=c++
cdef extern from "double_add.h":
    double cpp_double_add(double x, double y)

def py_double_add(double x, double y):
    return cpp_double_add(x, y)
```

This file is a python-like library, which imports C++ to Python.

## Step 1.3: Setup
Create a file named setup.py with the following content:

```python
# setup.py
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

extensions = [
    Extension("double_functions", 
              ["src/double_functions.pyx", "src/double_add.cpp"], # Extension name is used in import statement
              extra_compile_args=["-std=c++17"])
]

setup(
    name="cadd", # you can pip install this if you push it to PyPI
    ext_modules=cythonize(extensions)
)
```

## Step 1.4: Install and test your module
Run the following command to install your module:

```bash
pip install cadd_module
```

Then, create a file named test.py with the following content:

```python
import double_functions

print(double_functions.py_double_add(1, 2))
```

You should see the output `3` when you run the test.py file.