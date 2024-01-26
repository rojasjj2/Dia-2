def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("ingresa el numero para la serie fibonnaci n: "))
while n != 0:
    sequence = fibonacci(n)
    print(sequence)
    n = int(input("ingresa el valor de n (0 to exit): "))