import sympy as sp
from sympy.physics.vector import dynamicsymbols, init_vprinting
from IPython.display import Math, display

# Initialize printing
init_vprinting(use_latex='mathjax')

# Define symbols
t, t1, t2, c = sp.symbols('t t1 t2 c', real=True, positive=True)

# Define the acceleration function using piecewise
a_car = sp.Piecewise(
    (0, (t > 0) & (t < t1)),                    # a = 0 for 0 < t < t1
    (-c*(t - t1), (t >= t1) & (t < t2))         # a = -c(t - t1) for t1 < t < t2
)

print("Car acceleration function:")
print(r'a_c(t) = ' + sp.latex(a_car))

# Alternative: Include what happens after t2 (assuming acceleration = 0)
a_car_complete = sp.Piecewise(
    (0, (t <= 0) | (t >= t2)),                 # a = 0 for t ≤ 0 or t ≥ t2
    (0, (t > 0) & (t < t1)),                    # a = 0 for 0 < t < t1
    (-c*(t - t1), (t >= t1) & (t < t2))         # a = -c(t - t1) for t1 < t < t2
)

print("\nComplete acceleration function (including t ≥ t2):")
print(r'a_c(t) = ' + sp.latex(a_car_complete))

# Calculate velocity by integrating acceleration
# We need to handle the piecewise integration carefully
v_car = sp.integrate(a_car_complete, (t, 0, t))

print("\nVelocity function (integrated from t=0):")
print(r'v_c(t) = ' + sp.latex(v_car))

# Calculate position by integrating velocity
# For piecewise functions, we need to integrate each segment separately
# Position during first interval (0 ≤ t < t1): v = 0, so x = x0
x1 = sp.symbols('x1')  # Initial position at t=0

# Position during second interval (t1 ≤ t < t2)
# Integrate acceleration: v = ∫(-c(t-t1))dt = -c(t-t1)²/2
# Then integrate velocity: x = x1 + ∫v dt
x_car = sp.Piecewise(
    (x1, (t >= 0) & (t < t1)),  # Constant position during acceleration = 0
    (x1 - c*(t - t1)**3/6, (t >= t1) & (t < t2)),  # Position during deceleration
    (x1 - c*(t2 - t1)**3/6, t >= t2)  # Final position (constant after t2)
)

print("\nPosition function:")
print(r'x_c(t) = ' + sp.latex(x_car))

# Verify derivatives
print("\nVerification:")
v_from_x = sp.diff(x_car, t)
print("Velocity from position derivative:")
print(r'v(t) = ' + sp.latex(v_from_x))

a_from_v = sp.diff(v_from_x, t)
print("Acceleration from velocity derivative:")
print(r'a(t) = ' + sp.latex(a_from_v))

# Numerical example
print("\nNumerical example:")
values = {t1: 2.0, t2: 5.0, c: 3.0, x1: 0.0}

# Test at different times
test_times = [1.0, 2.5, 4.0, 6.0]
for test_t in test_times:
    a_val = a_car_complete.subs({**values, t: test_t})
    v_val = v_car.subs({**values, t: test_t})
    x_val = x_car.subs({**values, t: test_t})
    
    print(f"t = {test_t:.1f}s: a = {a_val:.2f} m/s², v = {v_val:.2f} m/s, x = {x_val:.2f} m")

# Alternative: Using dynamicsymbols
print("\nAlternative using dynamicsymbols:")
x_dynamic = dynamicsymbols('x')

# Create piecewise dynamicsymbol for acceleration
a_dynamic = sp.Piecewise(
    (0, (t > 0) & (t < t1)),
    (-c*(t - t1), (t >= t1) & (t < t2))
)

print("Acceleration with dynamicsymbol notation:")
print(r'a(t) = ' + sp.latex(a_dynamic))

# Key points about this acceleration function
print("\n=== KEY POINTS ===")
print("1. The acceleration is 0 during the first interval (coasting)")
print("2. The acceleration is negative during the second interval (braking)")
print("3. The braking acceleration increases linearly with time")
print("4. This represents a car that coasts, then brakes with increasing force")
print("5. The velocity will decrease quadratically during braking")
print("6. The position will decrease cubically during braking")
