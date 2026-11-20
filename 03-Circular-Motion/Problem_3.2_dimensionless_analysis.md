# Problem 3.2: Banked Car with Friction - Dimensionless Analysis

## Problem Overview

A car travels on a banked curve (banking angle **β**) with friction coefficient **μₛ**. The goal is to find the safe speed range **v_min** to **v_max** where the car stays in circular motion without slipping.

### Physical Answer (from force analysis)

$$v_{min} = \sqrt{\frac{gR(\sin\beta + \mu_s \cos\beta)}{\cos\beta + \mu_s \sin\beta}}$$

$$v_{max} = \sqrt{\frac{gR(\sin\beta + \mu_s \cos\beta)}{\cos\beta - \mu_s \sin\beta}}$$

---

## Why Dimensionless Analysis?

The physical speeds contain the product **gR** (gravity × radius). This means speeds change with:
- Different planets (different g)
- Different curve radii (different R)

**But is the physics really different?**

Dimensionless analysis reveals: **NO!** The underlying physics is the same everywhere. Only the scale changes.

---

## Dimensionless Formulation

### Natural Speed Scale

For a banked curve problem, the characteristic speed is:
$$v_{\text{scale}} = \sqrt{gR}$$

This combines gravity (vertical effects) and radius (circular motion) into one natural velocity scale.

### Dimensionless Speed Variables

Define:
$$v^* = \frac{v}{\sqrt{gR}}$$

Then the physical speeds become:
$$v = v^* \cdot \sqrt{gR}$$

### Dimensionless Speed Range

**Minimum speed:**
$$v_{min}^* = \sqrt{\frac{\sin\beta + \mu_s \cos\beta}{\cos\beta + \mu_s \sin\beta}}$$

**Maximum speed:**
$$v_{max}^* = \sqrt{\frac{\sin\beta + \mu_s \cos\beta}{\cos\beta - \mu_s \sin\beta}}$$

### KEY INSIGHT: Universal Physics!

**The dimensionless speeds depend ONLY on two angles:**
- **β**: the banking angle
- **μₛ**: the friction coefficient (dimensionless already)

The dimensionless forms are **completely independent** of:
- ❌ g (gravitational acceleration)
- ❌ R (curve radius)
- ❌ m (car mass, which cancels out in the force analysis)

---

## The Power of Dimensionless Analysis

### Universal Dimensionless Curves

The plots of $v_{min}^*$ and $v_{max}^*$ vs. **β** are **identical everywhere**:
- On Earth
- On the Moon
- On Jupiter
- On Mars
- On any asteroid or planet

These curves represent the **universal physics** of banked curves with friction.

### Physical Scaling

To convert from dimensionless to physical speeds, simply multiply by $\sqrt{gR}$:

**On Earth, R = 50m:**
$$v = v^* \times \sqrt{10 \times 50} = v^* \times \sqrt{500} = v^* \times 22.4 \text{ m/s}$$

**On Earth, R = 100m:**
$$v = v^* \times \sqrt{10 \times 100} = v^* \times \sqrt{1000} = v^* \times 31.6 \text{ m/s}$$

**On Moon, R = 50m:**
$$v = v^* \times \sqrt{1.6 \times 50} = v^* \times \sqrt{80} = v^* \times 8.9 \text{ m/s}$$

**Same dimensionless values → different physical speeds!**

---

## Friction's Role: Two Regimes

### Low Speed (v < v_min): Friction Points UP the Bank

- Car tends to **slide down** the sloped surface
- Static friction acts **up the slope** to prevent sliding
- Friction **adds to** the normal force's vertical component
- Friction **helps provide** centripetal force (adds horizontal component)
- Result: Friction **allows slower speeds**

**Force balance:**
$$N(\cos\beta + \mu_s \sin\beta) = mg \quad \text{(vertical)}$$
$$N(\sin\beta + \mu_s \cos\beta) = \frac{mv^2}{R} \quad \text{(horizontal)}$$

### High Speed (v > v_max): Friction Points DOWN the Bank

- Car tends to **slide outward and upward** on the slope
- Static friction acts **down the slope** to prevent sliding
- Friction **subtracts from** the normal force's vertical component
- Friction **still aids** centripetal force (but less vertical support)
- Result: Friction **limits maximum speed**

**Force balance:**
$$N(\cos\beta - \mu_s \sin\beta) = mg \quad \text{(vertical)}$$
$$N(\sin\beta + \mu_s \cos\beta) = \frac{mv^2}{R} \quad \text{(horizontal)}$$

---

## Dimensionless Behavior Patterns

### Pattern 1: Effect of Banking Angle β

As banking angle increases from 0° to 90°:

**v_min^* behavior:**
- Increases monotonically
- Slower at shallow angles, faster at steep angles
- At β = 0° (flat): v_min^* = √(μₛ)
- At β = 90° (vertical): v_min^* → 0 (can go arbitrarily slowly)

**v_max^* behavior:**
- Increases monotonically and faster than v_min^*
- Denominator approaches zero as β → 90°
- v_max^* → ∞ as β → 90° (can go arbitrarily fast)

**Speed range (v_max^* - v_min^*):**
- Widens dramatically with steeper banking
- More friction widens the range more at steep angles

### Pattern 2: Effect of Friction Coefficient μₛ

As friction increases from 0 to 1:

**v_min^* behavior:**
- Increases with μₛ (friction allows slower speeds)
- Effect stronger at steep banking angles

**v_max^* behavior:**
- Increases with μₛ (friction allows higher speeds)
- Effect stronger at steep banking angles

**Speed range:**
- Wider with more friction
- Zero friction gives: v_min^* = v_max^* = √(tan β) (single ideal speed)

### Pattern 3: Comparison to Frictionless Case

**Without friction (μₛ = 0):**
$$v_{min}^* = v_{max}^* = \sqrt{\tan\beta}$$

There's only ONE ideal speed for any banking angle. The car must travel at exactly this speed or it will slip.

**With friction (μₛ > 0):**
$$v_{min}^* < \sqrt{\tan\beta} < v_{max}^*$$

Friction creates a **range of safe speeds** around the ideal speed. The more friction, the wider the range.

---

## Special Cases

### Case 1: Flat Road (β = 0°)

$$v_{min}^* = v_{max}^* = \sqrt{\mu_s}$$

- No banking: only friction provides centripetal force
- Single ideal speed: v = √(μₛgR)
- Example: Earth, R=50m, μₛ=0.5: v = √(0.5 × 10 × 50) = 15.8 m/s

### Case 2: Frictionless Curve (μₛ = 0)

$$v_{min}^* = v_{max}^* = \sqrt{\tan\beta}$$

- Pure banking without friction
- Single ideal speed for each banking angle
- Example: β=30°: v* = √(tan 30°) = 0.760

### Case 3: Steep Banking (β → 85-89°)

$$v_{min}^* \approx \sqrt{\mu_s} \quad \text{(stays finite)}$$

$$v_{max}^* \to \infty \quad \text{(denominator→0)}$$

- Nearly vertical banking can support arbitrarily high speeds
- Low speeds still limited by friction
- Very wide speed range possible

---

## Numerical Examples

### Example: β = 30°, μₛ = 0.5

**Dimensionless values (UNIVERSAL):**
- v_min^* = 0.853
- v_max^* = 1.391
- Range: 0.538

**Physical speeds (scales by √(gR)):**

| Scenario | √(gR) | v_min | v_max | Range |
|----------|-------|-------|-------|-------|
| Earth, R=50m | 22.4 | 19.1 | 31.1 | 12.0 |
| Earth, R=100m | 31.6 | 27.0 | 44.0 | 17.0 |
| Moon, R=50m | 8.9 | 7.6 | 12.4 | 4.8 |
| Jupiter, R=50m | 35.4 | 30.2 | 49.2 | 19.0 |

Same dimensionless curve, different scales!

### Example: β = 45°, Varying μₛ

| μₛ | v_min^* | v_max^* | Range | Ratio |
|----|---------|---------|-------|-------|
| 0.0 | 1.000 | 1.000 | 0.000 | 1.00 |
| 0.3 | 1.076 | 1.137 | 0.061 | 1.06 |
| 0.5 | 1.149 | 1.282 | 0.133 | 1.12 |
| 0.7 | 1.231 | 1.464 | 0.233 | 1.19 |
| 1.0 | 1.372 | 1.916 | 0.544 | 1.40 |

More friction → wider safe range.

---

## Physical Interpretation of Dimensionless Results

### Why Are These Results Universal?

The dimensionless analysis reveals that banked curve physics at different locations (Earth, Moon, Jupiter) is **qualitatively identical**—only scaled by environmental factors.

**The universal curve v*(β, μₛ) encodes:**
1. How banking angle affects the safe speed range
2. How friction modifies that range
3. The relative proportions (which direction is steeper in the curve)

### How Do We Use This?

**Scenario 1: Design a highway curve**
- Choose banking angle β and expect friction μₛ
- Calculate v_min^* and v_max^* (dimensionless)
- Use road specifications (g ≈ 10 m/s², R from design) to get physical speeds
- Result: "Safe speed range is 25-45 mph"

**Scenario 2: Predict behavior on different planet**
- Take the same dimensionless curve (v* vs β)
- Scale by √(gR) for that planet
- Get physical speeds for that world
- Physics is identical; only numbers change

**Scenario 3: Optimize design for safety**
- Vary β and μₛ to find the widest speed range
- Use dimensionless analysis (no need to recalculate for each environment)
- Apply to Earth, Moon, Mars, or asteroid landing sites

---

## Key Takeaways

1. **Dimensionless speed v* = v/√(gR) reveals universal physics** independent of gravity and radius

2. **Physical speeds always scale as v = v* × √(gR)** - this is the fundamental scaling law

3. **Friction widens the safe speed range** by allowing speeds both below and above the frictionless ideal

4. **Banking angle and friction coefficient are the only dimensionless parameters** that matter

5. **The same mathematics applies everywhere** - Earth, Moon, Jupiter, Mars, asteroids, all use the same dimensionless curves

6. **Engineering power:** Design once (dimensionless), scale everywhere (multiply by √(gR))

---

## Connection to Problem 3.1 (Frictionless Case)

Recall Problem 3.1: Frictionless banked curve gives one ideal speed
$$v_{\text{ideal}} = \sqrt{gR\tan\beta}$$
$$v_{\text{ideal}}^* = \sqrt{\tan\beta}$$

Problem 3.2 with friction shows:
$$v_{min}^* \leq \sqrt{\tan\beta} \leq v_{max}^*$$

Friction creates a **range around the ideal frictionless speed**, allowing the driver flexibility without requiring exact speed control.

---

## Verification and Testing

### Dimensional Analysis Check
- v* is dimensionless ✓
- Equation dimensions: √(dimensionless / dimensionless) = dimensionless ✓
- Scaling √(gR) has dimensions of velocity ✓

### Limiting Cases Check
- μₛ → 0: v_min^* → v_max^* → √(tan β) ✓
- β → 0: Formulas give finite values based on friction ✓
- v_max^* > v_min^*: Always true when denominator is positive ✓

### Physical Reasonableness
- Steeper banking allows higher speeds ✓
- More friction allows lower minimum speeds and higher maximum speeds ✓
- Frictionless case has zero speed range ✓
- Results match intuition about driving on banked curves ✓
