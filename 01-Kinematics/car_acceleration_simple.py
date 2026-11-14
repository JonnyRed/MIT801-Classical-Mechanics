import sympy as sp

# Define symbols
t, t1, t2, c = sp.symbols('t t1 t2 c', real=True, positive=True)

# Your acceleration function
a_car = sp.Piecewise(
    (0, (t > 0) & (t < t1)),                    # a = 0 for 0 < t < t1
    (-c*(t - t1), (t >= t1) & (t < t2))         # a = -c(t - t1) for t1 < t < t2
)

print("Car acceleration function:")
print("a_c(t) = {")
print("    0,                     for 0 < t < t1")
print("    -c*(t - t1),           for t1 < t < t2")
print("}")

print("\nThis represents:")
print("- First interval: Car coasts with zero acceleration")
print("- Second interval: Car brakes with increasing deceleration")

# Show the symbolic form
print("\nSymbolic form:")
print(a_car)
