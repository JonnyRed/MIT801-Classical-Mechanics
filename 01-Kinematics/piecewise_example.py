import sympy as sp
from sympy.physics.vector import dynamicsymbols, init_vprinting
from IPython.display import Math, display

# Initialize printing
init_vprinting(use_latex='mathjax')

# Define time variable
t = sp.symbols('t', real=True)

# Method 1: Basic Piecewise function
# Example: Different values for different time intervals
f_piecewise = sp.Piecewise(
    (0, t < 0),                    # f(t) = 0 for t < 0
    (t, (t >= 0) & (t < 1)),       # f(t) = t for 0 ≤ t < 1
    (1, (t >= 1) & (t < 2)),       # f(t) = 1 for 1 ≤ t < 2
    (2 - t, (t >= 2) & (t < 3)),   # f(t) = 2 - t for 2 ≤ t < 3
    (0, t >= 3)                    # f(t) = 0 for t ≥ 3
)

print("Piecewise function:")
display(Math(r'f(t) = ' + sp.latex(f_piecewise)))

# Method 2: Using dynamicsymbols with Piecewise
# Create a dynamicsymbol that behaves differently in different intervals
x = dynamicsymbols('x')[0]

# Define piecewise dynamicsymbol
x_piecewise = sp.Piecewise(
    (0, t < 0),
    (t**2, (t >= 0) & (t < 1)),
    (2*t - 1, (t >= 1) & (t < 2)),
    (3, t >= 2)
)

print("\nDynamicsymbol with piecewise behavior:")
display(Math(r'x(t) = ' + sp.latex(x_piecewise)))

# Method 3: Vector with piecewise components
from sympy.physics.vector import ReferenceFrame

N = ReferenceFrame('N')

# Position vector with piecewise components
r_piecewise = sp.Piecewise(
    (t*N.x, (t >= 0) & (t < 1)),
    ((2 - t)*N.x + (t - 1)*N.y, (t >= 1) & (t < 2)),
    (N.y, t >= 2)
)

print("\nPosition vector with piecewise behavior:")
display(Math(r'\vec{r}(t) = ' + sp.latex(r_piecewise)))

# Method 4: Using Heaviside functions (alternative approach)
# Heaviside(t) = 0 for t < 0, 1 for t > 0
H = sp.Heaviside

# Create step functions
f_step = t * (H(t) - H(t-1)) + 1 * (H(t-1) - H(t-2)) + (2-t) * (H(t-2) - H(t-3))

print("\nUsing Heaviside step functions:")
display(Math(r'f(t) = ' + sp.latex(f_step)))

# Method 5: Differentiating piecewise functions
# Take derivatives of piecewise functions
f_derivative = sp.diff(f_piecewise, t)
print("\nDerivative of piecewise function:")
display(Math(r'f\'(t) = ' + sp.latex(f_derivative)))

# Method 6: Physics example - Force that changes over time
# Example: Force applied in different intervals
F_piecewise = sp.Piecewise(
    (0, t < 0),                           # No force before t=0
    (10*N.x, (t >= 0) & (t < 1)),         # Constant force for 0 ≤ t < 1
    (5*N.x, (t >= 1) & (t < 3)),         # Reduced force for 1 ≤ t < 3
    (0, t >= 3)                           # No force after t=3
)

print("\nPhysics example - Time-varying force:")
display(Math(r'\vec{F}(t) = ' + sp.latex(F_piecewise)))

# Method 7: Conditional expressions for dynamicsymbols
# Using sympy.logic for more complex conditions
from sympy.logic.boolalg import And, Or, Not

# Complex condition
f_complex = sp.Piecewise(
    (t**2, Or(t < 0, t > 2)),                           # t² for t < 0 or t > 2
    (sp.sin(t), And(t >= 0, t <= 1)),                   # sin(t) for 0 ≤ t ≤ 1
    (sp.exp(t), And(t > 1, t <= 2))                     # exp(t) for 1 < t ≤ 2
)

print("\nComplex conditional function:")
display(Math(r'f(t) = ' + sp.latex(f_complex)))

# Method 8: Evaluating piecewise functions
# Evaluate at specific points
print("\nEvaluation examples:")
for t_val in [-1, 0.5, 1.5, 2.5, 4]:
    result = f_piecewise.subs(t, t_val)
    print(f"f({t_val}) = {result}")

# Method 9: Plotting piecewise functions (if matplotlib available)
try:
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Create numerical function for plotting
    f_num = sp.lambdify(t, f_piecewise, 'numpy')
    
    # Generate points
    t_vals = np.linspace(-1, 4, 500)
    f_vals = f_num(t_vals)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals, f_vals, 'b-', linewidth=2)
    plt.grid(True, alpha=0.3)
    plt.xlabel('Time t')
    plt.ylabel('f(t)')
    plt.title('Piecewise Function')
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.show()
    
except ImportError:
    print("\nMatplotlib not available for plotting")

print("\nKey points for piecewise functions with dynamicsymbols:")
print("1. Use sp.Piecewise() for different expressions in different intervals")
print("2. Conditions use standard Python comparison operators")
print("3. Combine conditions with & (AND) and | (OR)")
print("4. Can differentiate piecewise functions (derivatives may have DiracDelta)")
print("5. Works with vectors and physics quantities")
print("6. Alternative: Use Heaviside step functions")
