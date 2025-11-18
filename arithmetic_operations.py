# Arithmetic operations on two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)

if b != 0:
    print("Quotient =", round(a / b, 2))
else:
    print("Division not possible (b = 0)")