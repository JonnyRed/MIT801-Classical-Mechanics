## Half Atwood Machine Analysis

We will analyze the system using two distinct techniques:

1. **The Work-Energy Theorem** ($W_{\text{net}} = \Delta K$)
2. **The Energy Balance / Conservation of Mechanical Energy Approach** ($\Delta E_{\text{mech}} = W_{\text{nc}}$)

### System Overview & Definitions

Consider a half Atwood machine with:

* $m_1$: Mass resting on the horizontal table.
* $m_2$: Hanging mass connected by a light, inextensible string over a pulley.
* $R$: Radius of the pulley.
* $I$: Moment of inertia of the pulley (e.g., $I = \frac{1}{2} m_p R^2$ for a uniform disk).
* $\mu_k$: Coefficient of kinetic friction between mass $m_1$ and the table.
* $\tau_f$: Constant rotational friction (bearing torque) opposing the pulley's rotation.
* $x$: Linear displacement of the system (distance $m_1$ moves toward the pulley, equal to the descent distance of $m_2$).
* $v = \dot{x}$: Linear speed of the masses.
* $\omega = \frac{v}{R}$: Angular speed of the pulley.

---

## Technique 1: The Work-Energy Theorem ($W_{\text{net}} = \Delta K$)

The Work-Energy Theorem states that the net work $W_{\text{net}}$ done by **all forces** (conservative and non-conservative, internal and external) on the system equals the change in total kinetic energy $\Delta K$:

$$W_{\text{net}} = \Delta K$$

### 1. Total Kinetic Energy ($K$)

The total kinetic energy of the system includes the translational kinetic energy of both masses and the rotational kinetic energy of the pulley:

$$K = \frac{1}{2} m_1 v^2 + \frac{1}{2} m_2 v^2 + \frac{1}{2} I \omega^2$$

Substituting $\omega = \frac{v}{R}$:

$$K = \frac{1}{2} \left( m_1 + m_2 + \frac{I}{R^2} \right) v^2$$

### 2. Work Done by Individual Forces Over Displacement $x$

* **Gravity on $m_2$** (Conservative): Does positive work as $m_2$ descends.

$$W_{g} = m_2 g x$$


* **Normal force and Gravity on $m_1$** (Conservative/Perpendicular): Do zero net work ($N = m_1 g$, perpendicular to motion).
* **Kinetic Friction on $m_1$** (Non-conservative): Opposes motion.

$$f_k = \mu_k N = \mu_k m_1 g$$


$$W_{\text{friction, table}} = -f_k x = -\mu_k m_1 g x$$


* **Rotational Friction Torque** (Non-conservative): Opposes angular motion through angular displacement $\theta = \frac{x}{R}$.

$$W_{\text{friction, pulley}} = -\tau_f \theta = -\tau_f \frac{x}{R}$$


* **Tension in the String** (Internal constraint forces): Internal tensions do equal and opposite work on connected parts and cancel out in the total system work calculation.

### 3. Net Work and Equation of Motion

Summing all contributing works:

$$W_{\text{net}} = m_2 g x - \mu_k m_1 g x - \frac{\tau_f}{R} x = \left( m_2 g - \mu_k m_1 g - \frac{\tau_f}{R} \right) x$$

Applying the Work-Energy Theorem ($W_{\text{net}} = \Delta K$ assuming starting from rest $K_i = 0$):

$$\left( m_2 g - \mu_k m_1 g - \frac{\tau_f}{R} \right) x = \frac{1}{2} \left( m_1 + m_2 + \frac{I}{R^2} \right) v^2$$

Differentiating both sides with respect to time $t$ (using $\frac{d}{dt}(\frac{1}{2} v^2) = v a$):

$$\left( m_2 g - \mu_k m_1 g - \frac{\tau_f}{R} \right) v = \left( m_1 + m_2 + \frac{I}{R^2} \right) v a$$

Cancelling $v$ yields the system acceleration $a$:

$$a = \frac{m_2 g - \mu_k m_1 g - \frac{\tau_f}{R}}{m_1 + m_2 + \frac{I}{R^2}}$$

---

## Technique 2: Conservation of Mechanical Energy ($\Delta E_{\text{mech}} = W_{\text{nc}}$)

When non-conservative forces (like kinetic friction and bearing torque) are present, total mechanical energy $E_{\text{mech}} = K + U$ is not conserved. Instead, the change in mechanical energy equals the work done by the **non-conservative forces** ($W_{\text{nc}}$):

$$\Delta E_{\text{mech}} = E_f - E_i = W_{\text{nc}}$$

### 1. Mechanical Energy Breakdown

* **Kinetic Energy ($K$)**:

$$K = \frac{1}{2} \left( m_1 + m_2 + \frac{I}{R^2} \right) v^2$$


* **Potential Energy ($U$)**: Taking the reference level at the final position of $m_2$ (descended by $x$):

$$U = m_2 g (h_0 - x)$$



Total mechanical energy at any state:

$$E_{\text{mech}} = \frac{1}{2} \left( m_1 + m_2 + \frac{I}{R^2} \right) v^2 + m_2 g (h_0 - x)$$

### 2. Non-Conservative Work ($W_{\text{nc}}$)

The non-conservative forces performing work on the system are table friction and bearing friction torque:

$$W_{\text{nc}} = W_{\text{friction, table}} + W_{\text{friction, pulley}} = -\mu_k m_1 g x - \frac{\tau_f}{R} x$$

### 3. Energy Balance Equation

Equating the change in mechanical energy $\Delta E_{\text{mech}} = E_{\text{mech}}(x) - E_{\text{mech}}(0)$ to $W_{\text{nc}}$:

$$\left[ \frac{1}{2} \left( m_1 + m_2 + \frac{I}{R^2} \right) v^2 + m_2 g (h_0 - x) \right] - \left[ 0 + m_2 g h_0 \right] = -\left( \mu_k m_1 g + \frac{\tau_f}{R} \right) x$$

Simplifying:

$$\frac{1}{2} \left( m_1 + m_2 + \frac{I}{R^2} \right) v^2 - m_2 g x = -\left( \mu_k m_1 g + \frac{\tau_f}{R} \right) x$$

Rearranging to solve for kinetic energy change confirms identical results to Technique 1:

$$\frac{1}{2} \left( m_1 + m_2 + \frac{I}{R^2} \right) v^2 = \left( m_2 g - \mu_k m_1 g - \frac{\tau_f}{R} \right) x$$

---

## Python / SymPy Implementation (`sympy.physics.vector`)

You can run this complete script in a Jupyter notebook cell inside VS Code. It uses `sympy.physics.mechanics` to set up the generalized coordinates, kinetic and potential energies, non-conservative generalized forces, and automatically derives the equations of motion via Lagrange's equations.

```python
# %% [markdown]
# # Half Atwood Machine Analysis with Friction using SymPy

# %%
import sympy as sp
from sympy.physics.mechanics import (
    ReferenceFrame,
    Particle,
    Point,
    LagrangesMethod,
    dynamicsymbols,
)

# Define symbols
t = sp.symbols('t')
m1, m2, I_p, R, g, mu_k, tau_f = sp.symbols(
    'm1 m2 I_p R g mu_k tau_f', positive=True
)

# Generalized coordinate (displacement x) and its time derivative (speed v)
x = dynamicsymbols('x')
v = dynamicsymbols('v')

# Inertial reference frame
N = ReferenceFrame('N')

# Define positions and velocities
# Let origin be at the pulley center.
# m1 moves horizontally by x, m2 descends vertically by x, pulley rotates by theta = x/R.
omega = x.diff(t) / R

# Kinetic Energy (K)
T_m1 = sp.Rational(1, 2) * m1 * x.diff(t) ** 2
T_m2 = sp.Rational(1, 2) * m2 * x.diff(t) ** 2
T_pulley = sp.Rational(1, 2) * I_p * omega**2
T_total = T_m1 + T_m2 + T_pulley

# Potential Energy (U) - taking m2 height as -x relative to datum
U_total = -m2 * g * x

# Lagrangian L = T - U
L = T_total - U_total

# Generalized non-conservative forces (Virtual work approach for non-conservative forces)
# Q_x = (Force_table_friction * delta_x + Torque_bearing * delta_theta) / delta_x
# delta_theta = delta_x / R
Q_nc = -mu_k * m1 * g - (tau_f / R)

# Set up Lagrange's method with non-conservative forces
q = [x]
# Using standard Lagrange formulation with generalized forces
# L.diff(q) - (d/dt)(L.diff(q_dot)) = Q_nc
mL = LagrangesMethod(L, q, forces=[(x, Q_nc)], frame=N)
eom = mL.form_lagranges_equations()

print('Equation of Motion (EOM):')
display(eom)

# Solve for acceleration (ddot{x})
accel_sol = sp.solve(eom[0], x.diff(t, 2))
print('\nDerived Acceleration (a = ddot{x}):')
display(accel_sol[0])

```

---

### Key Takeaways

1. **Kinetic Friction ($f_k$)** acts as a constant retarding force opposing the motion of $m_1$, scaled down by normal force $\mu_k m_1 g$.
2. **Rotational Friction ($\tau_f$)** at the pulley bearing introduces an effective linear retarding force of $\frac{\tau_f}{R}$ acting on the string.
3. Both non-conservative mechanisms directly reduce the net driving force ($m_2 g$), diminishing system acceleration and altering the mechanical energy balance identically across both analytical perspectives.