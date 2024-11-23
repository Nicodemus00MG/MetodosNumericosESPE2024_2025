
#? sumas y restas de vectores & matrices

#! numpy - ciencias de datos y calculo algebraico y lineal 
#? importando la libreria numpy como "np", alias "apodo", nombre a mi libreria 
import numpy as np

#? creacion de vector u & v

#! vectorBidemensional = np.array([[2,1,4,6],[1,6,7,5]]) 
u= np.array([0,9,1,8])
u = u.reshape(1, -1) #! dejar estandar vector fila

v= np.array([9,8,6,2])
v = v.reshape(1, -1) #! dejar estandar vector fila

#? creacion de mi variable suma1

suma1= u+v
#? impresion de respuesta suma1
print(suma1)

#? craecion de mi matriz A & B 

A= np.array([[8,3,4],[4,6,2],[1,5,2],[6,2,7]])
print(A)
B= np.array([[2,-1,1,3],[3,9,1,2],[5,1,4,6],[2,3,7,2]])
print("\n")
print(B)
# ! creacion de mi variable suma2
# ! el operador subtract permite hacer la diferencia de matrices

#! suma 2 , resta de matrices 

try:
   suma2= np.subtract(A,B)
except ValueError:
   suma2="Dimensiones incompatibles"
   
print(suma2)
    
    
#? producto matricial prodmtx1
try:
   prodmtx1= np.dot(u,v)
except ValueError :
    prodmtx1="Dimensiones incompatibles"


print("El producto matricial de u y v: ",prodmtx1)
#? producto matricial prodmtx2

#! crear transpuesta de v

vT = v.reshape(-1, 1) #!  transformar de una vector fila a un vector columna (quito fila y dejo columna)

print(f"\nTranspuesta de <v>: {vT}")
prodmtx2=np.dot(u,vT) 
print(f"\nProducto matricial de u*vT:\n {prodmtx2}")
#? producto matricial prodmtx3

try:
   prodmtx3= np.dot(A,B)
except ValueError :
    prodmtx3="Dimensiones incompatibles"


#? producto matricial prodmtx4


prodmtx4=np.dot(B,A) 
print(f"\nProducto matricial de BA:\n {prodmtx4}")

#? prodcu1= uv
prodcu1= u*v
print(f"\nproducto elemento a elemento de uv:\n {prodcu1}\n")
#? prodcu2= uTV
#* transpuesta de u : 
uT = u.reshape(-1, 1) #!  transformar de una vector fila a un vector columna (quito fila y dejo columna)

print(f"\ndimension u: {np.shape(u)}")
print(f"\ndimension uT: {np.shape(uT)}")
print("\ntranspuesta u: \n",uT)
prodcu2= uT*v
print(f"\nproducto elemento a elemento de uTv:\n {prodcu2}\n")

#? prodcu3= AB
try:
    prodcux3= A*B
    print(f"\nproducto elemento a elemento de AB:\n {prodcux3}\n")
except ValueError :
    prodcux3="Dimensiones incompatibles"
print(prodcux3)
