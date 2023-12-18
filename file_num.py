import numpy as file_num_module

a = file_num_module.array([0, 1, 2, 3, 4])
print(type(a))

b = file_num_module.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(b.dtype)

Y = file_num_module.array([[2,4],[6,8]])

Z= Y*2;
print(Z)

A = file_num_module.array([[0,1,1],[1,0,1]])
B = file_num_module.array ([[1,1],[1,1],[1,-1]])

print(A.ndim)
print(A.shape)

C = file_num_module.dot(A,B);
print(C) 

a=file_num_module.array([0,1])
b=file_num_module.array([1,0])
print(file_num_module.dot(a,b) )


X=file_num_module.array([[1,0],[0,1]])
Y=file_num_module.array([[2,1],[1,2]]) 
Z=file_num_module.dot(X,Y)
print(Z)