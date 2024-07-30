# scalar value

import numpy as np

a : np.ndarray = np.array(1000) # object to store

print(a) # prints
print(a.shape) # prints the shape of the object () = 0 -Denormalized
print(a.dtype) # prints the dtype of the object
print(type(a)) 
print(a.ndim) # prints the number of dimensions
print(a.size) # prints the size of the object
print(a.itemsize) # prints the itemsize of the object

# vector type

b : np.ndarray = np.array([1,2,3,4]) # object to store [1,2,3,4] = vector

print(f" object {b}") # prints
print(f"objec shape {b.shape}") # prints the shape of the object () = 0 -Denormalized
print(f" Object type {b.dtype}") # prints the dtype of the object
print(f"Object type with global function {type(b)}") # prints the dtype of the
print(f"Number of dimension {b.ndim}") # prints the number of dimensions
print(f"Total items in Array : {b.size}") # prints the size of the object
print(f"{b.itemsize}") # prints the itemsize of the object
