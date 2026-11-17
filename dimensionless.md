# Dimensionless

## Dimensionless Variables in Kinematics

| Quantity | Dimensionless Variable | Scaling Definition ($v_0 \neq 0, a \neq 0$) |
| :--- | :---: | :--- |
| Velocity | $v^*$ | $\displaystyle v^* = \frac{v}{v_0}$ |
| Time | $t^*$ | $\displaystyle t^* = \frac{at}{v_0}$ |
| Displacement | $s^*$ | $\displaystyle s^* = \frac{as}{v_0^2}$ |

### Derivation of Dimensionless Scaling Variables

**Goal:** Transform the standard kinematic equations into dimensionless form by identifying characteristic scales for velocity, time, and displacement.

#### Characteristic Scales

For a system with initial velocity $v_0$ and constant acceleration $a$:

* **Velocity scale:** $v_0$ (the initial velocity sets the natural velocity scale)
* **Time scale:** Acceleration is constant, so the characteristic time scale is $\frac{v_0}{a}$ (the time for acceleration $a$ to change velocity by $v_0$)
* **Displacement scale:** $\frac{v_0^2}{a}$ (the distance covered when velocity changes by $v_0$ under acceleration $a$)

### Justification: Why These Scales Are Not Arbitrary

These characteristic scales are **not guesses** — they emerge rigorously from **dimensional analysis** and **physical reasoning**. Here's why they are the unique, natural scales for this problem:

#### Method 1: Dimensional Analysis (Buckingham Pi Theorem)

The only available parameters in a constant-acceleration problem are $v_0$ and $a$. Any characteristic scale must be constructed from these using dimensional consistency.

**For Velocity $v^*$:**
- Dimensionally, the only way to form a dimensionless velocity is to divide two quantities with the same dimensions:
$$[v^*] = \frac{[LT^{-1}]}{[LT^{-1}]} = [1] \quad \Rightarrow \quad v^* = \frac{v}{v_0}$$

**For Time $t^*$:**
- We must combine $t$, $v_0$ [dimensions: $LT^{-1}$], and $a$ [dimensions: $LT^{-2}$] to eliminate dimensions:
$$\left[\frac{at}{v_0}\right] = \frac{[LT^{-2}][T]}{[LT^{-1}]} = \frac{[LT^{-1}]}{[LT^{-1}]} = [1] \quad \checkmark$$

This is the **unique** dimensionless combination:
$$t^* = \frac{at}{v_0}$$

**For Displacement $s^*$:**
- Similarly:
$$\left[\frac{as}{v_0^2}\right] = \frac{[LT^{-2}][L]}{[LT^{-1}]^2} = \frac{[L^2T^{-2}]}{[L^2T^{-2}]} = [1] \quad \checkmark$$

This is the **unique** dimensionless combination:
$$s^* = \frac{as}{v_0^2}$$

**Conclusion:** Dimensional analysis guarantees these are the *only* natural scales. Any other scaling would be dimensionally inconsistent with the problem's parameters.

#### Method 2: Physical Reasoning (Characteristic Scales)

**Velocity Scale:** $v_0$ is the given velocity reference — the initial speed defines the natural velocity scale for the problem.

**Time Scale:** The characteristic time is "how long does acceleration $a$ take to change velocity by $v_0$?"

From $v = v_0 + at$, when $v = 2v_0$ (a change of $v_0$ from initial):
$$2v_0 = v_0 + a \cdot t_{\text{char}} \quad \Rightarrow \quad t_{\text{char}} = \frac{v_0}{a}$$

**Displacement Scale:** The characteristic displacement is "how far do you travel in time $t_{\text{char}}$ under acceleration $a$?"

Using $v^2 = v_0^2 + 2as$ with final velocity $v = v_0$ (starting from rest):
$$v_0^2 = 0 + 2a \cdot s_{\text{char}} \quad \Rightarrow \quad s_{\text{char}} = \frac{v_0^2}{2a}$$

We drop the $\frac{1}{2}$ factor because dimensional analysis only cares about which parameter combinations are relevant (the numerical coefficient is a secondary detail):
$$s_{\text{char}} \sim \frac{v_0^2}{a}$$

**Conclusion:** Physical reasoning shows these scales emerge naturally as the "typical" values in the problem—they represent the amount of time and distance associated with velocity changes of order $v_0$.

#### Dimensionless Variable Definitions

Define dimensionless variables by normalizing physical quantities by their characteristic scales:

$$v^* = \frac{v}{v_0} \quad \text{(velocity normalized by initial velocity)}$$

$$t^* = \frac{t}{v_0/a} = \frac{at}{v_0} \quad \text{(time normalized by characteristic time scale)}$$

$$s^* = \frac{s}{v_0^2/a} = \frac{as}{v_0^2} \quad \text{(displacement normalized by characteristic displacement scale)}$$

#### Verification via Substitution

Starting with the velocity-time relation: $v = v_0 + at$

Divide both sides by $v_0$:
$$\frac{v}{v_0} = \frac{v_0 + at}{v_0} = 1 + \frac{at}{v_0}$$

Recognize that $\frac{at}{v_0} = t^*$ and $\frac{v}{v_0} = v^*$:
$$v^* = 1 + t^*$$

For displacement: $s = v_0 t + \frac{1}{2}at^2$

Divide both sides by $\frac{v_0^2}{a}$:
$$\frac{as}{v_0^2} = \frac{a(v_0 t + \frac{1}{2}at^2)}{v_0^2} = \frac{at}{v_0} + \frac{1}{2}\left(\frac{at}{v_0}\right)^2$$

Recognize $s^* = \frac{as}{v_0^2}$ and $t^* = \frac{at}{v_0}$:
$$s^* = t^* + \frac{1}{2}(t^*)^2$$

For the velocity-displacement relation: $v^2 = v_0^2 + 2as$

Square the dimensionless velocity and divide by $v_0^2$:
$$(v^*)^2 = \left(\frac{v}{v_0}\right)^2 = \frac{v^2}{v_0^2} = \frac{v_0^2 + 2as}{v_0^2} = 1 + \frac{2as}{v_0^2}$$

Recognize $\frac{2as}{v_0^2} = 2s^*$:
$$(v^*)^2 = 1 + 2s^*$$

| Standard Equation | Relation | Dimensionless Form |
| :--- | :---: | :--- |
| $v = v_0 + at$ | Velocity–Time | $v^* = 1 + t^*$ |
| $s = v_0t + \frac{1}{2}at^2$ | Displacement–Time | $s^* = t^* + \frac{1}{2}(t^*)^2$ |
| $v^2 = v_0^2 + 2as$ | Velocity–Displacement | $(v^*)^2 = 1 + 2s^*$ |
| $s = \frac{v + v_0}{2}t$ | Average Velocity Displacement | $\displaystyle s^* = \frac{v^* + 1}{2}t^*$ |

---

## Best Approach

1. Physical Reasoning First
2. Verify with Dimensional Analysis

In physics, the most effective strategy is **not** to choose between dimensional analysis and physical reasoning — it's to use both in a specific order:

### Why Physical Reasoning Should Lead

1. **Builds Intuition** — Understanding *why* a scale matters helps you develop physics intuition, which transfers to new and unfamiliar problems
2. **Reveals the Physics** — When you ask "how long does it take for $a$ to change velocity by $v_0$?", you're engaging with the *actual dynamics* of the problem, not just manipulating equations
3. **Easier to Remember** — You'll retain $t_{\text{char}} = \frac{v_0}{a}$ because you derived it from a physical insight, not memorized it from a formula
4. **Early Error Detection** — If your reasoning leads to a physically nonsensical result, you catch the mistake before formal verification

### Why Dimensional Analysis Is Your Safety Net

1. **Guarantees Correctness** — Dimensional inconsistency is impossible if you apply it properly
2. **Finds What You Missed** — When there are many parameters, dimensional analysis ensures you've identified all relevant combinations
3. **Works When Intuition Fails** — In unfamiliar domains (quantum mechanics, plasma physics, relativity), you may lack physical intuition but dimensional analysis still applies
4. **Professional Standard** — It's the rigorous check that separates educated guesses from justified derivations

### The Professional Physicist's Workflow

```
Physical Question
    ↓
Identify Relevant Parameters
    ↓
Physical Reasoning: "What's the natural scale?"
    ↓
Dimensional Analysis: "Did I get it right?"
    ↓
Verification: "Does the result make physical sense?"
```

**Example for this problem:**

| Step | Reasoning |
| --- | --- |
| **Physical Q** | "What's the characteristic time for velocity to change by $v_0$?" |
| **Parameters** | We have $v_0$ and $a$ |
| **Physical Answer** | From $v = v_0 + at$, when $\Delta v = v_0$: $t = \frac{v_0}{a}$ |
| **Dimensional Check** | $\left[\frac{v_0}{a}\right] = \frac{[LT^{-1}]}{[LT^{-2}]} = [T]$ ✓ |
| **Dimensionless Form** | $t^* = \frac{at}{v_0}$ makes the natural time scale implicit |

### Structuring Your Documentation

Lead with **physical reasoning** because that's how physicists think. Provide **dimensional analysis** as the rigorous justification:

> *"The characteristic time is $\frac{v_0}{a}$ because it answers the physical question: 'How long does acceleration $a$ take to change velocity by $v_0$?' This can be verified rigorously through dimensional analysis, which guarantees this is the unique dimensionless combination of $v_0$, $a$, and $t$."*
