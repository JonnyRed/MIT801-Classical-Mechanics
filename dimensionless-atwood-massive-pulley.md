# Dimensionless Atwood Machine with Massive Pulley

## Standard Solution (from WE3104)

For an Atwood machine with:
- Two hanging masses: $m_1$ and $m_2$ (assume $m_2 > m_1$)
- **Massive pulley** with radius $R$ and moment of inertia $I_A$ about center
- Inextensible, massless string
- Frictionless pulley

The acceleration is:
$$a = \frac{R^2 g(m_2 - m_1)}{I_A + R^2(m_1 + m_2)}$$

The tensions are:
$$T_1 = \frac{g m_1(I_A + 2R^2 m_2)}{I_A + R^2(m_1 + m_2)}$$

$$T_2 = \frac{g m_2(I_A + 2R^2 m_1)}{I_A + R^2(m_1 + m_2)}$$

---

## Dimensionless Form (Massive Pulley)

### Step 1: Identify All Parameters

| Parameter | Symbol | Dimension | Meaning |
| :--- | :---: | :---: | :--- |
| Mass 1 | $m_1$ | $M$ | Lighter hanging mass |
| Mass 2 | $m_2$ | $M$ | Heavier hanging mass |
| Pulley mass moment | $\frac{I_A}{R^2}$ | $M$ | Rotational inertia per unit radius |
| Gravity | $g$ | $LT^{-2}$ | Gravitational acceleration |
| Pulley radius | $R$ | $L$ | String radius |
| Reference length | $L$ | $L$ | System scale (optional) |

### Step 2: Rewrite Acceleration Formula

Divide numerator and denominator by $(m_1 + m_2)$:

$$a = \frac{R^2 g(m_2 - m_1)}{I_A + R^2(m_1 + m_2)} = \frac{R^2 g}{m_1 + m_2} \cdot \frac{m_2 - m_1}{\frac{I_A}{m_1 + m_2} + R^2}$$

Define the **dimensionless pulley moment**:
$$\beta = \frac{I_A/R^2}{m_1 + m_2}$$

This is the ratio of pulley's rotational inertia (per unit $R^2$) to the total translating mass.

Then:
$$a = g \cdot \frac{m_2 - m_1}{m_1 + m_2} \cdot \frac{1}{1 + \beta}$$

### Step 3: Define Dimensionless Variables

**Mass parameter** (unchanged from simple case):
$$\alpha = \frac{m_2 - m_1}{m_1 + m_2}$$

This satisfies $\alpha \in (-1, 1)$.

**Pulley inertia parameter:**
$$\beta = \frac{I_A/R^2}{m_1 + m_2}$$

This satisfies $\beta \geq 0$.

### Step 4: Dimensionless Acceleration

$$\boxed{a^* = \frac{a}{g} = \frac{\alpha}{1 + \beta}}$$

### Step 5: Characteristic Scales for Time and Velocity

Choose a **reference length** $L$ (e.g., how far a mass travels before constraint):

| Quantity | Characteristic Scale | Dimensionless Variable |
| :--- | :--- | :--- |
| **Acceleration** | $g$ | $a^* = \frac{a}{g}$ |
| **Velocity** | $v_0 = \sqrt{gL}$ | $v^* = \frac{v}{\sqrt{gL}}$ |
| **Time** | $t_0 = \sqrt{\frac{L}{g}}$ | $t^* = t\sqrt{\frac{g}{L}}$ |
| **Displacement** | $L$ | $s^* = \frac{s}{L}$ |

---

## Dimensionless Equations of Motion

### Kinematics (from constant acceleration)

Since $a^* = \frac{\alpha}{1 + \beta}$ is constant (dimensionless), the dimensionless motion equations are:

$$v^* = a^* \cdot t^* = \frac{\alpha}{1 + \beta} t^*$$

$$s^* = \frac{a^*}{2}(t^*)^2 = \frac{\alpha}{2(1 + \beta)}(t^*)^2$$

$$(v^*)^2 = 2a^* s^* = \frac{2\alpha}{1 + \beta}s^*$$

### Dimensionless Tensions

From the original equations:
$$T_1 = \frac{g m_1(I_A + 2R^2 m_2)}{I_A + R^2(m_1 + m_2)}$$

Divide by $(m_1 + m_2)g$:
$$T_1^* = \frac{T_1}{(m_1 + m_2)g} = \frac{\frac{m_1}{m_1 + m_2}(\beta + 2(1 - \alpha)/2)}{1 + \beta}$$

Simplify using $\frac{m_1}{m_1 + m_2} = \frac{1 - \alpha}{2}$:

$$\boxed{T_1^* = \frac{1 - \alpha}{2} \cdot \frac{\beta + 2 - \alpha}{1 + \beta}}$$

$$\boxed{T_2^* = \frac{1 + \alpha}{2} \cdot \frac{\beta + 2 + \alpha}{1 + \beta}}$$

---

## Physical Interpretation

### The Parameter $\beta$

**Key insight:** $\beta$ measures the **relative importance of pulley inertia**.

| Regime | $\beta$ | Physical Behavior |
| :--- | :--- | :--- |
| **Negligible pulley** | $\beta \to 0$ | $a^* \to \alpha$ (simple Atwood) |
| **Light pulley** | $\beta \ll 1$ | Small correction to simple case |
| **Comparable inertia** | $\beta \sim 1$ | Pulley and masses equally important |
| **Heavy pulley** | $\beta \gg 1$ | $a^* \to \frac{\alpha}{\beta} \to 0$ (sluggish) |
| **Infinite pulley** | $\beta \to \infty$ | $a^* \to 0$ (system locks up) |

### Why $\beta$ Emerges Naturally

From the acceleration formula:
$$a = \frac{R^2 g(m_2 - m_1)}{I_A + R^2(m_1 + m_2)}$$

The denominator has two competing terms:
- **Inertia to accelerate masses**: proportional to $m_1 + m_2$ (times $R^2$)
- **Inertia to rotate pulley**: $I_A$ (absolute)

The ratio $\beta = \frac{I_A/R^2}{m_1 + m_2}$ captures their **competition**.

---

## Common Pulley Geometries

For a uniform disk or cylinder of mass $m_A$ and radius $R$:
$$I_A = \frac{1}{2}m_A R^2$$

Then:
$$\beta = \frac{(1/2)m_A R^2 / R^2}{m_1 + m_2} = \frac{m_A}{2(m_1 + m_2)}$$

| Pulley Type | $I_A$ | $\beta$ |
| :--- | :--- | :--- |
| **Thin ring** | $m_A R^2$ | $\frac{m_A}{m_1 + m_2}$ |
| **Uniform disk** | $\frac{1}{2}m_A R^2$ | $\frac{m_A}{2(m_1 + m_2)}$ |
| **Hollow sphere** | $\frac{2}{3}m_A R^2$ | $\frac{2m_A}{3(m_1 + m_2)}$ |
| **Solid sphere** | $\frac{2}{5}m_A R^2$ | $\frac{2m_A}{5(m_1 + m_2)}$ |

---

## Comparison Table: Simple vs. Massive Pulley

| Aspect | Simple ($\beta = 0$) | With Pulley ($\beta > 0$) |
| :--- | :--- | :--- |
| **Acceleration** | $a = g\alpha$ | $a = \frac{g\alpha}{1+\beta}$ |
| **Dimensionless form** | $a^* = \alpha$ | $a^* = \frac{\alpha}{1+\beta}$ |
| **Parameter count** | 1 | 2 ($\alpha$, $\beta$) |
| **Effect of heavier mass** | Full acceleration | Reduced by factor $\frac{1}{1+\beta}$ |
| **Free fall limit** | $m_1 \to 0$: $a \to g$ | $m_1 \to 0$: $a \to \frac{g}{1+\beta}$ |
| **Equal mass case** | $a = 0$ (always) | $a = 0$ (always) |
| **Pulley torque** | $\tau = 0$ | $\tau = R(T_2 - T_1) \neq 0$ |

---

## Example: Numerical Analysis

### Setup
- $m_1 = 1$ kg (light mass)
- $m_2 = 3$ kg (heavy mass)
- Pulley: uniform disk, $m_A = 2$ kg, $R = 0.1$ m
- $g = 10$ m/s²
- Reference length: $L = 1$ m

### Calculate Parameters

**$\alpha$ (mass ratio):**
$$\alpha = \frac{3 - 1}{3 + 1} = \frac{2}{4} = 0.5$$

**$\beta$ (pulley effect):**
$$I_A = \frac{1}{2}m_A R^2 = \frac{1}{2}(2)(0.1)^2 = 0.01 \text{ kg m}^2$$

$$\beta = \frac{I_A/R^2}{m_1 + m_2} = \frac{0.01/0.01}{4} = \frac{1}{4} = 0.25$$

### Results

**Without pulley** ($\beta = 0$):
$$a_{\text{simple}} = g\alpha = 10 \times 0.5 = 5 \text{ m/s}^2$$

**With pulley** ($\beta = 0.25$):
$$a = \frac{g\alpha}{1+\beta} = \frac{10 \times 0.5}{1 + 0.25} = \frac{5}{1.25} = 4 \text{ m/s}^2$$

**Reduction factor:**
$$\frac{a_{\text{with pulley}}}{a_{\text{simple}}} = \frac{1}{1 + \beta} = \frac{1}{1.25} = 0.8 \text{ (20\% reduction)}$$

### Dimensionless Quantities

**Characteristic scales:**
- $t_0 = \sqrt{\frac{L}{g}} = \sqrt{\frac{1}{10}} = 0.316$ s
- $v_0 = \sqrt{gL} = \sqrt{10 \times 1} = 3.16$ m/s

**At time $t = 1$ s:**
- $t^* = 1 / 0.316 = 3.16$
- $v = a \cdot t = 4 \times 1 = 4$ m/s
- $v^* = 4 / 3.16 = 1.265$
- $s = \frac{1}{2}at^2 = \frac{1}{2}(4)(1)^2 = 2$ m
- $s^* = 2 / 1 = 2$

**Verification using dimensionless equations:**
$$s^* = \frac{\alpha}{2(1+\beta)}(t^*)^2 = \frac{0.5}{2(1.25)}(3.16)^2 = \frac{0.5}{2.5}(10) = 2 \quad \checkmark$$

$$(v^*)^2 = \frac{2\alpha}{1+\beta}s^* = \frac{2(0.5)}{1.25}(2) = \frac{1}{1.25}(2) = 1.6$$
$$v^* = \sqrt{1.6} = 1.265 \quad \checkmark$$

---

## Dimensionless Insight: Universal Behavior

### Key Result
**All Atwood machines with the same $(\alpha, \beta)$ are physically identical when rescaled.**

Example:
- System A: $m_1=1$ kg, $m_2=3$ kg, $m_A=2$ kg on Earth ($g=10$ m/s²)
- System B: $m_1=1$ ton, $m_2=3$ tons, $m_A=2$ tons on Moon ($g=1.6$ m/s²)

Both have the same $(\alpha=0.5, \beta=0.25)$ and thus identical **dimensionless motion**.

However, their **physical motion** differs:
- System A: $a = 4$ m/s², reaches speed after $t = 1$ s
- System B: $a = 0.64$ m/s², reaches same speed after $t = 6.25$ s

This is captured by rescaling the time and velocity scales by $\sqrt{\frac{g_B}{g_A}}$.

---

## Generalization: Beyond Simple Atwood

### With Air Resistance

If we include drag force $F_{\text{drag}} = -k v$, a new dimensionless group emerges:

$$\text{Drag parameter: } \gamma = \frac{k}{\sqrt{(m_1 + m_2)g L}}$$

The system now depends on **three** parameters: $(\alpha, \beta, \gamma)$.

### With Spring Support

If the pulley hangs from a spring with constant $K$:

$$\text{Spring parameter: } \kappa = \frac{K L}{(m_1 + m_2)g}$$

The system gains **three** parameters: $(\alpha, \beta, \kappa)$ and becomes more complex.

---

## Summary: Dimensionless Massive-Pulley Atwood

### Two Core Parameters

1. **$\alpha = \frac{m_2 - m_1}{m_1 + m_2}$** — Mass asymmetry ($-1 < \alpha < 1$)
2. **$\beta = \frac{I_A/R^2}{m_1 + m_2}$** — Pulley inertia effect ($\beta \geq 0$)

### Central Result

$$\boxed{a^* = \frac{a}{g} = \frac{\alpha}{1 + \beta}}$$

This **single formula** encapsulates how the pulley's mass **reduces acceleration** by a factor $\frac{1}{1+\beta}$.

### Physical Scaling

Once you specify $(\alpha, \beta)$ and choose a reference length $L$, all motion equations are determined:

$$s^* = \frac{\alpha}{2(1+\beta)}(t^*)^2, \quad v^* = \frac{\alpha}{1+\beta}t^*, \quad (v^*)^2 = \frac{2\alpha}{1+\beta}s^*$$

You can then **scale to any mass, gravity, or pulley geometry** by adjusting the characteristic time scale $t_0 = \sqrt{\frac{L}{g}}$.

### Why This Matters

The dimensionless form reveals:
- **What controls the system**: only $\alpha$ and $\beta$
- **Universal behavior**: all systems with the same $(\alpha, \beta)$ obey identical dynamics
- **Design insights**: if you want to slow the system, increase $\beta$ by using a heavier or larger-radius pulley
- **Scaling laws**: how the system behaves on different planets or at different length scales
