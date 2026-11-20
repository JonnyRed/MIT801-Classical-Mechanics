# Dimensionless Analysis: Banked Curve (Frictionless)

## Problem Statement

A car of mass $m$ is turning on a banked curve of angle $\phi$ with respect to the horizontal. The curve is icy and friction between the tires and the surface is negligible. The curve has a radius $r$. What is the speed $v$ at which the car can turn safely?

---

## Standard Solution

### Force Balance

**Vertical direction** (no acceleration):
$$N \cos\phi = mg$$

**Horizontal direction** (centripetal acceleration):
$$N \sin\phi = \frac{mv^2}{r}$$

### Solving for Speed

Divide the centripetal equation by the vertical equation:
$$\frac{N \sin\phi}{N \cos\phi} = \frac{mv^2/r}{mg}$$

$$\tan\phi = \frac{v^2}{rg}$$

$$v = \sqrt{rg\tan\phi}$$

**Key Observation:** The mass $m$ **cancels out completely!**

---

## Dimensionless Form

### Step 1: Identify All Parameters

| Parameter | Symbol | Dimension | Role |
| :--- | :---: | :---: | :--- |
| Curve radius | $r$ | $L$ | Geometric property |
| Gravitational acceleration | $g$ | $LT^{-2}$ | Natural acceleration scale |
| Banking angle | $\phi$ | $1$ | **Already dimensionless!** |
| Car mass | $m$ | $M$ | (Will cancel) |
| Safe speed | $v$ | $LT^{-1}$ | Quantity to find |

### Step 2: Dimensional Analysis (Buckingham Pi Theorem)

**Number of parameters:** 5 ($r$, $g$, $\phi$, $m$, $v$)

**Number of independent dimensions:** 2 ($L$, $T$) — note: **no mass dimension appears!**

**Number of independent dimensionless groups:** $5 - 2 = 3$

Since mass $m$ has dimension $M$ which does not appear in any other parameter, it cannot form a dimensionless group with the others. Therefore, **the solution cannot depend on $m$**.

### Step 3: Characteristic Velocity Scale

From the available parameters $r$ and $g$ (both are physical and have dimensions), we can form a unique velocity scale:

$$v_{\text{char}} = \sqrt{rg}$$

**Dimensional check:**
$$[v_{\text{char}}] = \sqrt{[L][LT^{-2}]} = \sqrt{[L^2T^{-2}]} = [LT^{-1}] \quad \checkmark$$

### Step 4: Dimensionless Velocity

Define the dimensionless velocity:
$$v^* = \frac{v}{v_{\text{char}}} = \frac{v}{\sqrt{rg}}$$

Substitute the physical solution $v = \sqrt{rg\tan\phi}$:

$$v^* = \frac{\sqrt{rg\tan\phi}}{\sqrt{rg}} = \sqrt{\tan\phi}$$

### **Central Result**

$$\boxed{v^* = \sqrt{\tan\phi}}$$

---

## Physical Interpretation

### Independence from Mass

The elegant result shows that **the safe turning speed is independent of the car's mass**. This occurs because:

1. Heavier cars require proportionally more centripetal force: $F_c \propto m v^2 / r$
2. The normal force providing this force is also proportional to mass: $N \propto m$
3. These mass factors exactly cancel in the force balance equation
4. The result depends **only on the geometric angle** $\phi$

### Independence from Radius and Gravity

The result is also independent of:
- **Curve radius $r$**: Larger curves can safely accommodate higher speeds, but only by factor $\sqrt{r}$
- **Gravitational field $g$**: Weaker gravity allows higher speeds, but only by factor $\sqrt{g}$

These dependencies are **captured entirely by the characteristic scale** $\sqrt{rg}$.

---

## Numerical Example

### Setup
- Banking angle: $\phi = 30°$
- Curve radius: $r = 50$ m
- Gravitational acceleration: $g = 10$ m/s²
- Car mass: $m = 1500$ kg (irrelevant to result)

### Calculation

**Dimensionless velocity:**
$$v^* = \sqrt{\tan 30°} = \sqrt{\frac{1}{\sqrt{3}}} = \sqrt{0.5774} \approx 0.760$$

**Characteristic scale:**
$$v_{\text{char}} = \sqrt{rg} = \sqrt{50 \times 10} = \sqrt{500} \approx 22.36 \text{ m/s}$$

**Physical speed:**
$$v = v^* \times v_{\text{char}} = 0.760 \times 22.36 \approx 17.0 \text{ m/s} \approx 61 \text{ km/h}$$

### Verification

Using the direct formula:
$$v = \sqrt{rg\tan\phi} = \sqrt{50 \times 10 \times \tan 30°} = \sqrt{500 \times 0.5774} = \sqrt{288.7} \approx 17.0 \text{ m/s} \quad \checkmark$$

---

## Universal Scaling

### Key Insight: Universality

**All frictionless banked curves with the same banking angle $\phi$ have the same dimensionless speed**, regardless of:
- The curve's radius
- The gravitational field
- The car's mass

### Scaling Between Different Systems

| Property | System A (Earth) | System B (Moon) |
| :--- | :--- | :--- |
| **Banking angle** | $\phi = 30°$ | $\phi = 30°$ |
| **Radius** | $r = 50$ m | $r = 50$ m |
| **Gravity** | $g = 10$ m/s² | $g = 1.6$ m/s² |
| **Dimensionless speed** | $v^* = \sqrt{\tan 30°} = 0.760$ | $v^* = \sqrt{\tan 30°} = 0.760$ |
| **Physical speed** | $v = 17.0$ m/s | $v = 6.75$ m/s |
| **Time scale** | $t_0 = \sqrt{r/g} = 2.24$ s | $t_0 = \sqrt{r/g} = 5.59$ s |

**Interpretation:** On the Moon, with weaker gravity, the safe turning speed is **lower** (6.75 vs. 17.0 m/s), but the **dimensionless speed is identical**. The difference is encoded in the characteristic time scale.

---

## Characteristic Scales for Complete Motion Analysis

If we include time-dependent analysis (how the car approaches the curve):

| Quantity | Characteristic Scale | Dimensionless Variable |
| :--- | :--- | :--- |
| **Velocity** | $v_{\text{char}} = \sqrt{rg}$ | $v^* = \frac{v}{\sqrt{rg}}$ |
| **Time** | $t_{\text{char}} = \sqrt{\frac{r}{g}}$ | $t^* = t\sqrt{\frac{g}{r}}$ |
| **Tangential acceleration** | $a_{\text{char}} = g$ | $a^* = \frac{a_t}{g}$ |
| **Angular frequency** | $\omega_{\text{char}} = \sqrt{\frac{g}{r}}$ | $\omega^* = \omega\sqrt{\frac{r}{g}}$ |

---

## Comparison Table: Physics Insight

| Scenario | Formula | Dimensionless Form |
| :--- | :--- | :--- |
| **Increasing $\phi$** | $v \propto \sqrt{\tan\phi}$ | $v^*$ increases |
| **Increasing $r$** | $v \propto \sqrt{r}$ | $v^* = \sqrt{\tan\phi}$ (unchanged) |
| **Increasing $g$** | $v \propto \sqrt{g}$ | $v^* = \sqrt{\tan\phi}$ (unchanged) |
| **Increasing $m$** | $v$ independent of $m$ | $v^*$ independent of $m$ |

**Key takeaway:** Only the **banking angle** affects the dimensionless speed. All other factors scale the characteristic velocity scale $\sqrt{rg}$.

---

## Generalization: With Friction

If friction is present (coefficient $\mu$):

The safe speed becomes:
$$v = \sqrt{\frac{rg(\mu + \tan\phi)}{1 - \mu\tan\phi}}$$

### Dimensionless Form with Friction

**New dimensionless group:** The friction coefficient $\mu$ (itself dimensionless)

**Dimensionless velocity:**
$$v^* = \sqrt{\frac{\mu + \tan\phi}{1 - \mu\tan\phi}}$$

**New parameters controlling the system:** 2
- $\phi$ (banking angle)
- $\mu$ (friction coefficient)

**Physical insight:** Friction becomes another dimensionless parameter, increasing system complexity. The result now depends on **both** the geometry and the material properties of the road surface.

---

## Dimensional Analysis Method Summary

### Why Dimensionless Analysis Works Here

1. **Problem structure**: Only dimensions $L$ and $T$ appear (no mass dependence)
2. **Parameter count**: 5 parameters, 2 independent dimensions
3. **Dimensionless groups**: 3 independent combinations
4. **Constraints**: Only one combination can relate $v$, $r$, $g$; $\phi$ is already dimensionless
5. **Result**: The solution is uniquely determined up to $\phi$

### Steps to Dimensionless Solution

| Step | Action | Result |
| :--- | :--- | :--- |
| 1 | List all parameters | $r, g, \phi, m, v$ |
| 2 | Identify dimensions | Only $L, T$ (no $M$) |
| 3 | Apply Buckingham Pi | $5 - 2 = 3$ groups |
| 4 | Form characteristic scale | $v_{\text{char}} = \sqrt{rg}$ |
| 5 | Define dimensionless variable | $v^* = \frac{v}{\sqrt{rg}}$ |
| 6 | Use physics constraint | $\tan\phi = \frac{v^2}{rg}$ gives $v^* = \sqrt{\tan\phi}$ |

---

## Summary

| Aspect | Result |
| :--- | :--- |
| **Dimensionless speed** | $v^* = \sqrt{\tan\phi}$ |
| **Physical speed** | $v = \sqrt{rg\tan\phi}$ |
| **Parameters controlling motion** | Only $\phi$ (and $\mu$ if friction present) |
| **Mass dependence** | None—cancels in force balance |
| **Key insight** | Physics depends **only on geometry**, not on mass or scale |
| **Characteristic scale** | $v_0 = \sqrt{rg}$ |
| **Characteristic time** | $t_0 = \sqrt{\frac{r}{g}}$ |

---

## Physical Implications

### For Road Design

- A road banked at $45°$ permits $v^* = \sqrt{\tan 45°} = 1$ (dimensionless)
- Physical speed depends entirely on curve radius and gravity
- **On Earth** at $r = 100$ m: $v = \sqrt{100 \times 10 \times 1} = \sqrt{1000} \approx 31.6$ m/s ≈ 114 km/h
- **On Moon** at same curve: $v \approx 7.9$ m/s — much slower due to weaker gravity

### For Vehicle Dynamics

- Car mass is **irrelevant** for safe speed on a frictionless banked curve
- A motorcycle and an 18-wheeler can safely travel at the same dimensionless speed
- Their actual speeds differ only by the factor $\sqrt{rg}$

### For Physics Education

This problem demonstrates:
- **Power of dimensional analysis**: Reveals what truly matters
- **Mass cancellation**: Not all parameters affect all results
- **Universal behavior**: Systems with same dimensionless parameters are physically identical
- **Scaling laws**: How results change with geometry and gravitational field
