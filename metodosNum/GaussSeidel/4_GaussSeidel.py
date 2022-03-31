# Gauss Seidel 

#Definicion de las ecuaciones en la forma de la diagonal dominante
f1 = lambda x,y,z: (3 + y + z)/6
f2 = lambda x,y,z: (40 - 6*x - z)/9
f3 = lambda x,y,z: (50 + 3*x - y)/-12

# Iniciamos a la variables en 0
x0 = 0
y0 = 0
z0 = 0
count = 1 #contador para mostrar las iteraciones

# Leer valor tolerable
e = float(input('Ingresa Error Tolerable: '))

#impresion del renglon titulo
print('\Contador\tx\ty\tz\n')

condition = True

#ciclo while
while condition:
    #evaluamos las 3 ecuaciones
    x1 = f1(x0,y0,z0)
    y1 = f2(x1,y0,z0)
    z1 = f3(x1,y1,z0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' %(count, x1,y1,z1))
    #calculamos el error relativo de las 3 variables
    e1 = abs((x1-x0)/x1);
    e2 = abs((y1-y0)/y1);
    e3 = abs((z1-z0)/z1);
    #x1 es equivalente a x_i, x0 es equivalente a x_i-1
    
    count += 1 #al contador se le suma 1
    #asignamos el valor de las variables al la variable anterior 
    x0 = x1
    y0 = y1
    z0 = z1
    
    #mientras los errores de las 3 variables sean mayor al valor dado
    #el ciclo se seguira repitiendo
    condition = e1>e and e2>e and e3>e

#imprimimos la solucion
print('\nSolucion: x=%0.3f, y=%0.3f, z = %0.3f\n'% (x1,y1,z1))