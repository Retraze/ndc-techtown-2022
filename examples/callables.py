# A standard function, it is indeed callable

def compute_polynomial(a, b, c, x):
    print(f"Computing the polynomial of {a}^2 + {b}x + {c}...")
    return a*x**2 + b*x + c

print(
    compute_polynomial(4, 3, 2, 5)
)


# A standard lambda function, it is also indeed callable

compute_polynomial = lambda a, b, c, x: a*x**2 + b*x + c
print(
    compute_polynomial(4, 3, 2, 5)
)

# A callable class. It implements __call__, makings its instances callable

class Polynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __call__(self, x):
        print(f"Computing the polynomial of {self.a}^2 + {self.b}x + {self.c}...")
        return self.a*x**2 + self.b*x + self.c

polynomial = Polynomial(4, 3, 2)
print(
    polynomial(5)
)


# Functionally equivalent, using the captured closure instead of self

Polynomial = lambda a, b, c: lambda x: a*x**2 + b*x + c

polynomial = Polynomial(4, 3, 2)
print(
    polynomial(5)
)
