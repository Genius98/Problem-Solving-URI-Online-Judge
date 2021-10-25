A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159

Triangle = 1 / 2 * A * C
Circle = pi * C * C
Trapezium = 1 / 2 * (A + B) * C
square = B * B
rectangle = A * B
print("TRIANGULO: %.3f" % Triangle)
print("CIRCULO: %.3f" % Circle)
print("TRAPEZIO: %.3f" % Trapezium)
print("QUADRADO: %.3f" % square)
