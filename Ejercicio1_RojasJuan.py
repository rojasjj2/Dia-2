def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print("bienvenido usuario")
print("ingresa un numero para crear la serie de fibonnaci")
print("te explico, la serie fibonnaci es una secuencia de numeros")
print("ejemplo: si colocas el numero 5, se van a sumar lo demas numeros que trae atras osea 0, 1, 1, 2, 3")
 


n = int(input("ingresa el numero para la serie fibonnaci n: "))
while n != 0:
    sequence = fibonacci(n)
    print(sequence)
    n = int(input("ingrese un nuevo número de datos a mostrar, o si quiere salir presione cero '0': "))







