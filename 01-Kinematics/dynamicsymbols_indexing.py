import sympy as sp
from sympy.physics.vector import dynamicsymbols, init_vprinting
from IPython.display import Math, display

# Initialize printing
init_vprinting(use_latex='mathjax')

print("=== WHY DYNAMYMBOLS ARE INDEXED ===\n")

# 1. Basic dynamicsymbols (returns a tuple)
print("1. Creating dynamicsymbols:")
x_symbols = dynamicsymbols('x')
print(f"dynamicsymbols('x') returns: {type(x_symbols)} = {x_symbols}")

# 2. Multiple dynamicsymbols at once
print("\n2. Multiple dynamicsymbols:")
xyz_symbols = dynamicsymbols('x y z')
print(f"dynamicsymbols('x y z') returns: {type(xyz_symbols)} = {xyz_symbols}")

# 3. Accessing individual symbols
print("\n3. Accessing individual symbols:")
x = xyz_symbols[0]  # First symbol (x)
y = xyz_symbols[1]  # Second symbol (y)  
z = xyz_symbols[2]  # Third symbol (z)
print(f"x = xyz_symbols[0] = {x}")
print(f"y = xyz_symbols[1] = {y}")
print(f"z = xyz_symbols[2] = {z}")

# 4. Why indexing is useful - Vector components
print("\n4. Vector components using indexing:")
t = sp.symbols('t')

# Create position vector components
x_pos, y_pos, z_pos = dynamicsymbols('x y z')

# Position vector
r = x_pos*sp.Matrix([1, 0, 0]) + y_pos*sp.Matrix([0, 1, 0]) + z_pos*sp.Matrix([0, 0, 1])
print("Position vector r = x(t)i + y(t)j + z(t)k")
display(Math(r'\vec{r}(t) = ' + sp.latex(r)))

# 5. Time derivatives using indexing
print("\n5. Time derivatives:")
v = sp.diff(r, t)  # Velocity vector
a = sp.diff(v, t)  # Acceleration vector

print("Velocity:")
display(Math(r'\vec{v}(t) = ' + sp.latex(v)))
print("Acceleration:")
display(Math(r'\vec{a}(t) = ' + sp.latex(a)))

# 6. Multiple particles/systems
print("\n6. Multiple particles - why indexing is essential:")
# Create position symbols for multiple particles
r1_symbols = dynamicsymbols('x1 y1 z1')  # Particle 1
r2_symbols = dynamicsymbols('x2 y2 z2')  # Particle 2

r1_x, r1_y, r1_z = r1_symbols
r2_x, r2_y, r2_z = r2_symbols

print("Particle 1 position components:")
print(f"r1_x = {r1_x}, r1_y = {r1_y}, r1_z = {r1_z}")
print("Particle 2 position components:")
print(f"r2_x = {r2_x}, r2_y = {r2_y}, r2_z = {r2_z}")

# 7. Generalized coordinates in Lagrangian mechanics
print("\n7. Generalized coordinates (Lagrangian mechanics):")
q_symbols = dynamicsymbols('q1 q2 q3 q4')  # 4 generalized coordinates
q1, q2, q3, q4 = q_symbols

print("Generalized coordinates:")
print(f"q₁ = {q1}, q₂ = {q2}, q₃ = {q3}, q₄ = {q4}")

# 8. Alternative: Single dynamicsymbol
print("\n8. Alternative: Single dynamicsymbol:")
x_single = dynamicsymbols('x')[0]  # Get just one symbol
print(f"dynamicsymbols('x')[0] = {x_single}")

# 9. Using with time derivatives
print("\n9. Time derivatives of indexed dynamicsymbols:")
x_dot = sp.diff(x_single, t)
x_ddot = sp.diff(x_dot, t)
print(f"ẋ = {x_dot}")
print(f"ẍ = {x_ddot}")

# 10. Comparison with regular symbols
print("\n10. Comparison: dynamicsymbols vs regular symbols:")
x_regular = sp.Function('x')(t)  # Regular function of time
x_dynamic = dynamicsymbols('x')[0]  # Dynamicsymbol

print(f"Regular function: {x_regular}")
print(f"Dynamicsymbol: {x_dynamic}")
print(f"Derivative of regular: {sp.diff(x_regular, t)}")
print(f"Derivative of dynamic: {sp.diff(x_dynamic, t)}")

print("\n=== KEY REASONS FOR INDEXING ===")
print("1. **Batch creation**: Create multiple related symbols at once")
print("2. **Consistency**: All symbols share the same time variable")
print("3. **Vector components**: Easy to create x, y, z components")
print("4. **Multiple particles**: Track different particles with indexed symbols")
print("5. **Generalized coordinates**: Perfect for q₁, q₂, q₃... in mechanics")
print("6. **Memory efficiency**: More efficient than creating symbols individually")
print("7. **Physics conventions**: Matches textbook notation (x₁, x₂, x₃)")

print("\n=== COMMON USAGE PATTERNS ===")
print("# Position components:")
print("x, y, z = dynamicsymbols('x y z')")
print("")
print("# Multiple particles:")  
print("r1 = dynamicsymbols('x1 y1 z1')")
print("r2 = dynamicsymbols('x2 y2 z2')")
print("")
print("# Generalized coordinates:")
print("q = dynamicsymbols('q1:5')  # q1, q2, q3, q4")
print("")
print("# Single symbol:")
print("x = dynamicsymbols('x')[0]")
