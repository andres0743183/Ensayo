import numpy

matriz =  numpy.matrix(numpy.empty(shape=(0,3), dtype=int))
for i in range(3):
    matriz=numpy.insert(matriz, i, [i + 1, 0, 0], axis = 0)
    
    
a = np.array([[1, 1], [2, 2], [3, 3]])


np.insert(a, 1, 5)
array([1, 5, 1, 2, 2, 3, 3])
np.insert(a, 1, 5, axis=1)
array([[1, 5, 1],
       [2, 5, 2],
       [3, 5, 3]])
    
    
    np.insert(a, 1, 5, axis=1)