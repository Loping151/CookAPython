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