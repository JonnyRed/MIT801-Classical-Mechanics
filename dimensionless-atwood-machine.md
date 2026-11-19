# Dimensionless Atwood Machine

## Standard Atwood Machine Setup

The classic **Atwood machine** consists of:
- Two masses $m_1$ and $m_2$ (assume $m_2 > m_1$)
- Connected by an inextensible string over a pulley
- For the **simple case** (massless pulley, no friction):

The acceleration of the system is:
$$a = \frac{(m_2 - m_1)g}{m_1 + m_2}$$

The tension in the string is:
$$T = \frac{2m_1 m_2 g}{m_1 + m_2}$$

---

## Dimensionless Variables for the Atwood Machine

To identify the natural dimensionless parameters, we use **dimensional analysis** on the available parameters:

| Quantity | Dimension | Available |
| :--- | :---: | :--- |
| Mass 1 | $M$ | $m_1$ |
| Mass 2 | $M$ | $m_2$ |
| Gravitational acceleration | $LT^{-2}$ | $g$ |
| String tension | $MLT^{-2}$ | $T$ |
| System acceleration | $LT^{-2}$ | $a$ |
| Time | $T$ | $t$ |
| Displacement | $L$ | $s$ |

### Key Dimensionless Groups (Buckingham Pi Theorem)

The number of **independent dimensionless groups** is:
$$n_{\pi} = n_{\text{parameters}} - n_{\text{dimensions}} = 5 - 2 = 3$$

#### Group 1: Mass Ratio

The only way to form a dimensionless ratio from two masses:
$$\mu = \frac{m_2}{m_1} \quad \text{(dimensionless)}$$

Or, the **asymmetry parameter**:
$$\alpha = \frac{m_2 - m_1}{m_1 + m_2} \in (-1, 1)$$

This can be inverted to show $\mu = \frac{1 + \alpha}{1 - \alpha}$.

**Physical Interpretation:**
- $\alpha = 0$ → Equal masses, **no acceleration**
- $\alpha \to 1$ → $m_2 \gg m_1$ → $a \to g$ (free fall)
- $\alpha \to -1$ → $m_1 \gg m_2$ → $a \to -g$ (reversal)

#### Group 2: Characteristic Acceleration Scale

From gravity and the mass ratio, the natural acceleration scale is:
$$a_{\text{char}} = g$$

The dimensionless acceleration is:
$$a^* = \frac{a}{g} = \frac{(m_2 - m_1)}{m_1 + m_2}$$

**For the simple Atwood machine:**
$$a^* = \alpha$$

#### Group 3: Characteristic Time Scale

With characteristic acceleration $a_{\text{char}} = g$ and a length scale $L$ (not yet specified), the time scale is:
$$t_{\text{char}} = \sqrt{\frac{L}{g}}$$

This is the time for gravity to accelerate an object over distance $L$.

**More naturally**, if we want to study when the system reaches its characteristic speed, we might use:
$$t_{\text{char}} = \frac{v_{\text{char}}}{g} = \frac{\sqrt{gL}}{g} = \sqrt{\frac{L}{g}}$$

---

## Dimensionless Form of Atwood Machine Equations

### Case 1: Constant Acceleration (Massless Pulley)

Starting with:
$$a = g\alpha$$

where $\alpha = \frac{m_2 - m_1}{m_1 + m_2}$.

If we introduce a **reference length** $L$ (e.g., the distance one mass travels before hitting the floor), then:

**Dimensionless variables:**
$$t^* = t\sqrt{\frac{g}{L}} \quad \text{(time)}$$

$$s^* = \frac{s}{L} \quad \text{(displacement)}$$

$$v^* = \frac{v}{\sqrt{gL}} \quad \text{(velocity)}$$

**Dimensionless equations:**
$$v^* = \alpha \cdot t^*$$

$$s^* = \frac{\alpha}{2}(t^*)^2$$

$$(v^*)^2 = 2\alpha \cdot s^*$$

**Result:** The dynamics are **completely characterized by the single parameter $\alpha$**. All other details follow from dimensional consistency.

---

### Case 2: With Massive Pulley (Complete Analysis)

For a **massive pulley** with moment of inertia $I_A$ and radius $R$:

The acceleration becomes:
$$a = \frac{(m_2 - m_1)g}{m_1 + m_2 + \frac{I_A}{R^2}}$$

#### Dimensionless Groups

**Mass parameter (unchanged):**
$$\alpha = \frac{m_2 - m_1}{m_1 + m_2}$$

**Pulley inertia parameter:**
$$\beta = \frac{I_A/R^2}{m_1 + m_2}$$

This is the **dimensionless moment of inertia** — it represents how much the pulley's rotational inertia resists the motion compared to the translating masses.

**Dimensionless acceleration:**
$$a^* = \frac{a}{g} = \frac{\alpha}{1 + \beta}$$

#### Physical Interpretation of $\beta$

- $\beta = 0$ → Massless pulley (ideal case)
- $\beta \ll 1$ → Light pulley (small correction)
- $\beta \sim 1$ → Pulley inertia comparable to masses
- $\beta \gg 1$ → Heavy pulley dominates (acceleration $\approx 0$)

---

## Complete Dimensionless System

### Parameters

| Symbol | Meaning | Range |
| :--- | :--- | :--- |
| $\alpha = \frac{m_2 - m_1}{m_1 + m_2}$ | Mass asymmetry | $\in (-1, 1)$ |
| $\beta = \frac{I_A/R^2}{m_1 + m_2}$ | Pulley inertia parameter | $\in [0, \infty)$ |

### Characteristic Scales

| Quantity | Characteristic Scale | Dimensionless Variable |
| :--- | :--- | :--- |
| **Acceleration** | $g$ | $a^* = \frac{a}{g}$ |
| **Velocity** | $\sqrt{gL}$ | $v^* = \frac{v}{\sqrt{gL}}$ |
| **Time** | $\sqrt{\frac{L}{g}}$ | $t^* = t\sqrt{\frac{g}{L}}$ |
| **Displacement** | $L$ | $s^* = \frac{s}{L}$ |
| **Tension** | $(m_1 + m_2)g$ | $T^* = \frac{T}{(m_1 + m_2)g}$ |

**Result for simple Atwood machine:**
$$a^* = \alpha$$
$$T^* = \frac{2}{1 + \mu}$$
where $\mu = \frac{m_2}{m_1}$ is the mass ratio.

---

## Example: Numerical Dimensionless Solution

### Setup
- $m_1 = 1$ kg
- $m_2 = 3$ kg
- $g = 10$ m/s²
- $L = 2$ m
- Massless pulley ($\beta = 0$)

### Calculation

**Mass parameter:**
$$\alpha = \frac{3 - 1}{3 + 1} = \frac{2}{4} = 0.5$$

**Characteristic scales:**
- Acceleration scale: $g = 10$ m/s²
- Time scale: $\sqrt{\frac{L}{g}} = \sqrt{\frac{2}{10}} = 0.447$ s
- Velocity scale: $\sqrt{gL} = \sqrt{10 \times 2} = 4.47$ m/s

**Physical results:**
- Acceleration: $a = 0.5 \times 10 = 5$ m/s²
- After $t = 1$ s: $v = 5$ m/s, $s = 2.5$ m

**Dimensionless results:**
- Dimensionless acceleration: $a^* = \frac{5}{10} = 0.5$ (equals $\alpha$ ✓)
- Dimensionless time: $t^* = 1 \times \sqrt{\frac{10}{2}} = 2.236$
- Dimensionless velocity: $v^* = \frac{5}{4.47} = 1.118$
- Dimensionless displacement: $s^* = \frac{2.5}{2} = 1.25$

**Verification using dimensionless equations:**
$$s^* = \frac{\alpha}{2}(t^*)^2 = \frac{0.5}{2}(2.236)^2 = 0.25 \times 5 = 1.25 \quad \checkmark$$

$$(v^*)^2 = 2\alpha s^* = 2 \times 0.5 \times 1.25 = 1.25 \quad \Rightarrow \quad v^* = 1.118 \quad \checkmark$$

---

## Physical Insights from Dimensionless Analysis

### 1. The System Has Only One True Degree of Freedom

Once you specify **$\alpha$ (the mass ratio)** and **$\beta$ (the pulley effect)**, the entire dynamics are determined up to a choice of:
- Reference length $L$ (determines time and velocity scales)
- Initial conditions (position and velocity)

### 2. Universality: All Systems with Same $\alpha$ Behave Identically

An Atwood machine with $m_1 = 1$ g, $m_2 = 3$ g on **Earth** behaves identically (dimensionlessly) to one with $m_1 = 1$ ton, $m_2 = 3$ tons on **the Moon** — if we scale time and length appropriately!

### 3. Symmetry and Reversal

If you **reverse** the mass labels ($m_1 \leftrightarrow m_2$), then:
$$\alpha_{\text{new}} = \frac{m_1 - m_2}{m_1 + m_2} = -\alpha_{\text{old}}$$

The acceleration **reverses direction**, as expected.

---

## Comparison: Simple vs. Massive Pulley

| Aspect | Simple (Massless) | With Massive Pulley |
| :--- | :--- | :--- |
| **Acceleration** | $a = g\alpha$ | $a = g\frac{\alpha}{1 + \beta}$ |
| **Parameter count** | 1 ($\alpha$) | 2 ($\alpha$, $\beta$) |
| **Characteristic scale** | $g$ | $g$ |
| **Pulley torque** | $\tau = 0$ (tension is equal) | $\tau = R(T_2 - T_1)$ |
| **Energy storage** | Only in masses | In masses + pulley rotation |

---

## Applications and Generalizations

### 1. With Air Resistance

Add a drag term: $F_{\text{drag}} = -kv$

**Dimensionless drag parameter:**
$$\gamma = \frac{k}{\sqrt{(m_1 + m_2)gL}}$$

This creates an additional dimensionless group, increasing complexity.

### 2. With Spring Support

If the pulley hangs from a spring with constant $K$:

**Dimensionless spring parameter:**
$$\kappa = \frac{K}{(m_1 + m_2)g/L}$$

### 3. With Friction

If there's friction at the pulley: coefficient of friction $\mu_f$

The acceleration becomes nonlinear, and $\mu_f$ enters as an additional parameter.

---

## Summary: Dimensionless Atwood Machine

The **dimensionless formulation** reveals that:

1. **Two parameters control everything**: $\alpha$ (mass ratio) and $\beta$ (pulley inertia)
2. **One length scale** must be chosen: either the initial separation or the distance to some constraint
3. **All motion equations simplify** to depend only on dimensionless time $t^*$ and $\alpha, \beta$
4. **Physical predictions scale correctly** with units automatically

For a **given choice of $\alpha$ and $\beta$**, you can:
- Predict the dimensionless motion $s^*(t^*)$
- Scale up or down by changing $L$ (and thus time scale $\sqrt{L/g}$)
- Apply to any gravitational field (Earth, Moon, Jupiter) by adjusting $g$
- Apply to systems of any mass scale

**The beauty of dimensionless analysis**: the Atwood machine's essential physics is captured by **a single parameter** (or two, if the pulley is massive).
