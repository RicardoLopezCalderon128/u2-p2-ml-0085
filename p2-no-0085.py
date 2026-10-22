import numpy as np
# Ricardo Lopez NC 0085
# ejemplos de numpy
print("--Especiado Linealmente en array -- 0085")
arre=np.linspace(start=0, stop=5, num=5)
print(arre)
print("--matriz identidad en 2array -- 0085")
matrix=np.eye(3)
print(matrix)
print("--genera numeros al azar(aleatorios) en 2D array -- 0085")
numale=np.random.random((3,4))  # genera 12 numeros aleatorios 
print(numale)
print("genera 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3))  
print(numale)
# como generar 9 numeros aleatorios comprendidos entre 1 y 20
# con numpy en un arreglo de 3 por 3
print("generar 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=(3, 3))
print(arre)
print("Ricardo lopez NC 0085 ")