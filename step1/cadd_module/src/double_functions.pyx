# distutils: language=c++
cdef extern from "double_add.h":
    double cpp_double_add(double x, double y)

def py_double_add(double x, double y):
    return cpp_double_add(x, y)