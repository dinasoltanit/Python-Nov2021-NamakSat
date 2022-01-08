import numpy as np

x = np.array([[1,2],[3,4]])
print(x)
y = np.array([[5,6],[7,8]])
print(y)

v = np.array([9,10])
print(v)
w = np.array([11, 12])
print(w)

# Inner product of vectors; both produce 219
print(v.dot(w))
print(w.dot(v))
print(np.dot(v, w))
vw = np.dot(v, w)
# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
xv = np.dot(x, v)
# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
xy = np.dot(x, y)