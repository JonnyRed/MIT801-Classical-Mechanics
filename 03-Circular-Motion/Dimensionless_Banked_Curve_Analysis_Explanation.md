# Dimensionless Banked Curve Analysis - Notebook Explanation

## Overview
This Jupyter notebook demonstrates the analysis of **banked curve dynamics** using **dimensionless analysis**. It shows how to find the optimal speed for a vehicle traversing a banked curve without friction, and how this speed scales across different gravitational environments.

## Physical Problem

### The Scenario
A vehicle travels on a banked curve (like a highway ramp or race track). The curve is tilted at an angle **φ** (phi) to the horizontal. The analysis assumes:
- **No friction** between the tires and road
- Only two forces act on the vehicle: gravity and the normal force from the road
- The vehicle moves at constant speed in a circular path of radius **r**

### Key Physics
For a banked curve without friction, the optimal speed (ideal banking speed) occurs when the normal force alone provides both:
1. The vertical support against gravity
2. The horizontal centripetal force needed for circular motion

At this speed, the vehicle doesn't require friction to maintain its trajectory.

## Dimensionless Analysis Approach

### Why Dimensionless?
The notebook uses **dimensionless analysis** to separate the universal physics from specific environmental parameters. This reveals:
- **Universal behavior** that applies everywhere (every planet, every radius)
- **Physical scaling** that shows how to scale from one scenario to another

### The Dimensionless Speed Variable

The notebook defines:
$$v^* = \frac{v}{\sqrt{gr}}$$

Where:
- **v** = physical speed (m/s)
- **g** = gravitational acceleration (m/s²)
- **r** = curve radius (m)
- **v*** = dimensionless speed (unitless)

### Key Finding
The optimal banking speed depends **only on the banking angle φ**:

$$v^* = \sqrt{\tan(\phi)}$$

This remarkable result shows that the relationship between banking angle and dimensionless speed is **universal** - it applies to:
- Earth, the Moon, Jupiter, or any planet
- Small curves (r = 50m) or large curves (r = 100m)

## Notebook Structure and Operation

### Setup Phase
The notebook imports scientific libraries:
- **NumPy**: numerical arrays and mathematical functions
- **Matplotlib**: plotting and visualization
- **SciPy**: optimization and special functions (if used)

### Mathematical Functions

#### 1. **Dimensionless Speed Calculation**
```python
def dimensionless_speed(phi_rad):
    return np.sqrt(np.tan(phi_rad))
```
Takes banking angle in radians and returns v* = √(tan φ)

#### 2. **Physical Speed Calculation**
```python
def physical_speed(phi_rad, r, g):
    return np.sqrt(r * g * np.tan(phi_rad))
```
Converts the dimensionless relationship to actual speeds using radius r and gravity g

### Analysis Steps

#### Step 1: Angle Array Creation
The notebook creates a range of banking angles from 0° to 85° and converts them to radians for calculation.

#### Step 2: Dimensionless Curve
Calculates v* for each angle using the universal formula v* = √(tan φ). This curve is **identical for all environments**.

#### Step 3: Physical Scenarios
For comparison, the notebook defines multiple scenarios:
- **Earth, r=50m**: highway curve on Earth
- **Earth, r=100m**: larger highway curve on Earth
- **Moon, r=50m**: same radius curve on the Moon (g = 1.6 m/s²)
- **Jupiter, r=50m**: same radius curve on Jupiter (g = 25 m/s²)

#### Step 4: Physical Speed Calculations
For each scenario, it calculates actual speeds v = √(gr tan φ) across all banking angles.

### Visualization

The notebook produces **two side-by-side plots**:

#### **Left Plot: Dimensionless Form**
- Plots v* vs banking angle φ
- Shows the **universal behavior**
- One curve that applies everywhere
- Demonstrates that at 45°, the dimensionless speed equals 1
- Increasing curve (non-linear): small angles require low speeds, steep angles require high speeds

#### **Right Plot: Physical Form**
- Plots actual speed (m/s) vs banking angle φ
- Shows four different curves for the four scenarios
- Demonstrates **physical scaling**:
  - Moon curve is lowest (weakest gravity)
  - Earth curves are in the middle
  - Jupiter curve is highest (strongest gravity)
  - Larger radius curves require higher speeds
- Same shape as the dimensionless plot, but with different scales

### Output Table

The notebook generates a comprehensive table showing:

#### Dimensionless Values (Universal)
- v* at φ = 30°: 0.7598
- v* at φ = 45°: 1.0000
- v* at φ = 60°: 1.3161

#### Physical Speeds for Each Scenario (at three banking angles)
Demonstrates how physical speed scales:
- **Moon is slower** than Earth (lower gravity)
- **Jupiter is faster** than Earth (higher gravity)
- **Larger radius curves require higher speeds** (more distance to cover per unit time)

## Key Insights Demonstrated

### 1. **Universal Dimensionless Relationship**
The curve on the left plot is identical for all scenarios - this demonstrates the power of dimensionless analysis.

### 2. **Physical Scaling**
Given v*, you can calculate physical speed for **any** situation:
$$v = v^* \cdot \sqrt{gr}$$

### 3. **Comparison Across Environments**
- Earth 50m: 16.99 m/s at 30°
- Moon 50m: 6.80 m/s at 30° (60% slower)
- Jupiter 50m: 26.86 m/s at 30° (58% faster)

### 4. **Engineering Application**
Designers can use v* to:
- Scale results from wind tunnel testing to real conditions
- Design curves for different planets or asteroids
- Predict optimal speeds without recalculating physics for each scenario

## Mathematical Derivation (Implicit in Notebook)

For a banked curve without friction:
- Vertical force balance: N cos(φ) = mg
- Horizontal force balance: N sin(φ) = mv²/r

Dividing these equations:
$$\tan(\phi) = \frac{v^2}{gr}$$

Therefore:
$$v = \sqrt{gr \tan(\phi)}$$

Defining v* = v/√(gr) gives:
$$v^* = \sqrt{\tan(\phi)}$$

## Conclusion

This notebook elegantly demonstrates:
1. **How dimensionless analysis reveals universal physics** (the left plot)
2. **How to scale results to any real scenario** (the right plot)
3. **How the same physics applies everywhere**, just with different numerical values
4. **Practical engineering**: the dimensionless form allows designing for any environment by simply scaling one universal relationship

The key takeaway: understanding the **dimensionless form** provides physical insight and predictive power for the **physical scenarios**.
