# Problem 3.2: Banked Car with Friction - Solution Explanation

## Problem Statement

A car of mass **m** travels around a circular turn of radius **R** on a banked curve tilted at angle **β** to the horizontal. The car experiences friction with coefficient of static friction **μₛ**. Find the range of speeds **v_min** to **v_max** required to keep the car moving in a circle without slipping.

**Given:**
- m: mass of car
- R: radius of circular turn
- β: banking angle
- μₛ: coefficient of static friction
- g: gravitational acceleration

**Find:** v_min and v_max

---

## Physical Setup and Force Analysis

### The Forces
Three forces act on the car (assuming the wheels don't slip):

1. **Weight (mg)**: Acts vertically downward
2. **Normal Force (N)**: Acts perpendicular to the road surface
3. **Friction Force (f)**: Acts tangentially on the road surface

### Force Components

Since the road is banked at angle **β**, the normal force and friction force can be decomposed:

#### Normal Force Components:
- **Horizontal (toward center):** N sin(β)
- **Vertical (upward):** N cos(β)

#### Friction Force Components:
The friction acts either **up** or **down** the banking depending on the speed:

- **Friction pointing up the bank (at high speed):**
  - Horizontal: f cos(β) (toward center)
  - Vertical: f sin(β) (upward)

- **Friction pointing down the bank (at low speed):**
  - Horizontal: -f cos(β) (away from center)
  - Vertical: -f sin(β) (downward)

### Circular Motion Requirement

For the car to maintain circular motion at speed **v**:
- **Centripetal force needed:** mv²/R (directed toward center)
- **Vertical equilibrium:** No vertical acceleration

---

## Case 1: Minimum Speed (Friction Points Up the Bank)

At **low speeds**, the car tends to slip down the bank. Friction acts **up the slope** to prevent this.

### Force Equations (vertical and horizontal)

**Vertical equilibrium:**
$$N \cos(\beta) + f \sin(\beta) = mg$$

**Horizontal (centripetal):**
$$N \sin(\beta) + f \cos(\beta) = \frac{mv^2}{R}$$

### Maximum Static Friction

The magnitude of static friction is limited:
$$f = \mu_s N$$

### Solving for v_min

Substitute f = μₛN into the vertical equation:
$$N \cos(\beta) + \mu_s N \sin(\beta) = mg$$
$$N(\cos(\beta) + \mu_s \sin(\beta)) = mg$$
$$N = \frac{mg}{\cos(\beta) + \mu_s \sin(\beta)}$$

Substitute this into the horizontal equation:
$$N \sin(\beta) + \mu_s N \cos(\beta) = \frac{mv_{min}^2}{R}$$
$$N(\sin(\beta) + \mu_s \cos(\beta)) = \frac{mv_{min}^2}{R}$$

Substitute the expression for N:
$$\frac{mg(\sin(\beta) + \mu_s \cos(\beta))}{\cos(\beta) + \mu_s \sin(\beta)} = \frac{mv_{min}^2}{R}$$

**Solving for v_min:**
$$v_{min} = \sqrt{\frac{gR(\sin(\beta) + \mu_s \cos(\beta))}{\cos(\beta) + \mu_s \sin(\beta)}}$$

---

## Case 2: Maximum Speed (Friction Points Down the Bank)

At **high speeds**, the car tends to slip up and outward on the bank. Friction acts **down the slope** to prevent this.

### Force Equations (vertical and horizontal)

**Vertical equilibrium:**
$$N \cos(\beta) - f \sin(\beta) = mg$$

**Horizontal (centripetal):**
$$N \sin(\beta) + f \cos(\beta) = \frac{mv^2}{R}$$

(Note: The friction now points down, so it subtracts from vertical and subtracts from the centripetal component)

Actually, let me reconsider the signs. When friction points down the bank:
- Vertical component is DOWNWARD, so it opposes the normal force's vertical component
- Horizontal component still points toward the center (down the slope is radially inward at the bottom)

**Corrected vertical equilibrium:**
$$N \cos(\beta) - f \sin(\beta) = mg$$

**Horizontal (centripetal):**
$$N \sin(\beta) + f \cos(\beta) = \frac{mv^2}{R}$$

(Both normal and friction point generally toward center)

### Solving for v_max

Using f = μₛN:
$$N \cos(\beta) - \mu_s N \sin(\beta) = mg$$
$$N(\cos(\beta) - \mu_s \sin(\beta)) = mg$$
$$N = \frac{mg}{\cos(\beta) - \mu_s \sin(\beta)}$$

Substitute into horizontal equation:
$$N \sin(\beta) + \mu_s N \cos(\beta) = \frac{mv_{max}^2}{R}$$
$$N(\sin(\beta) + \mu_s \cos(\beta)) = \frac{mv_{max}^2}{R}$$

$$\frac{mg(\sin(\beta) + \mu_s \cos(\beta))}{\cos(\beta) - \mu_s \sin(\beta)} = \frac{mv_{max}^2}{R}$$

**Solving for v_max:**
$$v_{max} = \sqrt{\frac{gR(\sin(\beta) + \mu_s \cos(\beta))}{\cos(\beta) - \mu_s \sin(\beta)}}$$

---

## Final Answer

The safe speed range for the car is:

$$\boxed{v_{min} = \sqrt{\frac{gR(\sin(\beta) + \mu_s \cos(\beta))}{\cos(\beta) + \mu_s \sin(\beta)}}}$$

$$\boxed{v_{max} = \sqrt{\frac{gR(\sin(\beta) + \mu_s \cos(\beta))}{\cos(\beta) - \mu_s \sin(\beta)}}}$$

---

## Physical Interpretation

### Key Observations

1. **Identical Numerators**
   - Both v_min and v_max have the same numerator: gR(sin β + μₛ cos β)
   - This represents the centripetal force available from both normal and friction forces
   - The difference lies only in whether friction opposes or aids the normal force vertically

2. **Denominators Show Vertical Support**
   - v_min denominator: cos β + μₛ sin β (maximum vertical support)
   - v_max denominator: cos β - μₛ sin β (minimum vertical support)
   - The friction coefficient appears additively in v_min (friction helps support weight)
   - The friction coefficient appears subtractively in v_max (friction opposes vertical support)

3. **Speed Range Width**
   - The range v_max - v_min widens as β increases
   - The range narrows as μₛ decreases (less friction → narrower safe range)
   - At μₛ = 0 (no friction): v_max - v_min is very large

### Special Cases

#### Case 1: No Banking (β = 0)
$$v_{min} = v_{max} = \sqrt{gR\mu_s}$$
- Only friction provides centripetal force
- Single ideal speed, no range

#### Case 2: No Friction (μₛ = 0)
$$v_{min} = v_{max} = \sqrt{gR\tan(\beta)}$$
- Only normal force provides support and centripetal force
- Returns to the frictionless banked curve problem
- Single ideal speed (the case from the dimensionless banked curve analysis)

#### Case 3: Steep Banking (β → 90°)
$$v_{min} \approx \sqrt{gR\mu_s}$$
$$v_{max} \to \infty$$
- Nearly vertical banking
- Friction is essential at low speeds
- Very high speeds still possible

---

## Friction's Role

### At v_min (Low Speed):
- Car tends to **slide down** the bank
- **Static friction acts up** the slope
- Friction **increases** the vertical component of support
- Friction **aids** the normal force in providing centripetal force
- Result: Friction **allows slower speeds**

### At v_max (High Speed):
- Car tends to **slide up and outward** the bank
- **Static friction acts down** the slope
- Friction **decreases** the vertical component of support
- Friction **aids** the normal force in providing centripetal force (but less vertical support available)
- Result: Friction **limits maximum speed**

---

## Solution Strategy Summary

1. **Identify the direction** of friction for each speed regime
   - Low speed → friction up the slope
   - High speed → friction down the slope

2. **Write force equations** for both vertical and horizontal directions
   - Vertical: Forces must sum to zero (no vertical acceleration)
   - Horizontal: Forces must provide centripetal acceleration mv²/R

3. **Apply friction constraint:** f ≤ μₛN (equality at the limiting speeds)

4. **Solve for N** in terms of given parameters using the vertical equation

5. **Substitute N** into the centripetal force equation

6. **Solve for v** to get v_min and v_max

---

## Verification

You can verify these expressions by checking:

1. **Dimensional analysis**: Both expressions have dimensions of velocity ✓
2. **Limiting cases**: 
   - As μₛ → 0, both formulas should approach √(gR tan β) ✓
   - As β → 0, the formulas should give √(gRμₛ) for horizontal track ✓
3. **Physical reasonableness**: v_max > v_min always (when denominators are positive) ✓

