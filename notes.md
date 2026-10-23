# Physics Notes

## Kinematic Motion

$
\boxed{
    \begin{aligned}
        \frac{d v}{d t} &= a(t) \\
        v_f - v_i &= \int^{t_1}_{t_0} a d t
    \end{aligned}
}
$

----

$
\boxed{
    \begin{aligned}
        a(v) &= \frac{d v}{d t} \\
        a(v) &= \frac{d v}{d x} \frac{d x}{d t} \\
        a(v) &= v \frac{d v}{d x} \\
        dx & = \frac{v d v}{a(v)} \\
        \int_{x_0}^{x_1} dx &= \int_{v_0}^{v_1} \frac{v d v}{a(v)} \implies  
        x_f - x_i = \int_{v_i}^{v_f} \frac{v d v}{a(v)}
    \end{aligned}
}
$

----

$
\boxed{
    \begin{aligned}
        a(x) &= \frac{d v}{d t} \\
        a(x) &= \frac{d v}{d x} \frac{d x}{d t}  \\
        a(x) &= v \frac{d v}{d x} \\
        a(x) dx &= v d v \\
        \int_{x_i}^{x_f} a(x) dx &= \int_{v_i}^{v_f} v d v \implies
        {v_f^2} - {v_i^2} = 2 \cdot \int_{x_0}^{x_1} a(x) dx  \\
    \end{aligned}
}
$

## Moments of Inertia

# Common Moments of Inertia

The moment of inertia, $I$, measures how difficult it is to change an object's rotational motion about a specified axis.

The following Markdown table lists common shapes, with $M$ representing mass, $R$ radius, $L$ length, and $h$ height.

| Object                        | Axis of rotation                         | Moment of inertia, $I$                                                          |
| ----------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------- |
| Point mass                    | Distance $r$ from axis                   | $I=Mr^2$                                                                         |
| Thin hoop or ring             | Through centre, perpendicular to plane   | $I=MR^2$                                                                         |
| Solid disc                    | Through centre, perpendicular to plane   | $I=\frac{1}{2}MR^2$                                                              |
| Solid cylinder                | Longitudinal axis                        | $I=\frac{1}{2}MR^2$                                                              |
| Hollow cylinder (thin-walled) | Longitudinal axis                        | $I=MR^2$                                                                         |
| Solid sphere                  | Through centre                           | $I=\frac{2}{5}MR^2$                                                              |
| Thin spherical shell          | Through centre                           | $I=\frac{2}{3}MR^2$                                                              |
| Thin rod                      | Through centre, perpendicular to rod     | $I=\frac{1}{12}ML^2$                                                             |
| Thin rod                      | Through one end, perpendicular to rod    | $I=\frac{1}{3}ML^2$                                                              |
| Rectangular plate             | Through centre, perpendicular to plate   | $I=\frac{1}{12}M(a^2+b^2)$                                                       |
| Solid rectangular block       | Through centre, parallel to side $L$     | $I=\frac{1}{12}M(a^2+b^2)$, where $a,b$ are the perpendicular dimensions         |
| Annular disc (thick ring)     | Through centre, perpendicular to plane   | $I=\frac{1}{2}M(R_o^2+R_i^2)$                                                    |

## Important points

- The axis matters: the same object can have different moments of inertia about different axes.
- Mass farther from the axis increases $I$: mass at a greater distance contributes proportionally to the square of that distance.
- Units: the SI unit is $\mathrm{kg\,m^2}$.

### Two useful formulas

For a collection of point masses,

$$
I=\sum_i m_i r_i^2
$$

For a continuous body,

$$
I=\int r^2\,dm
$$

### The parallel-axis theorem

If you know the moment of inertia about an axis through the centre of mass, you can calculate it about a parallel axis a distance $d$ away:

$$
\boxed{I=I_{\mathrm{cm}}+Md^2}
$$

For your Atwood-machine studies: a pulley modelled as a uniform solid disc has $I=\frac12 MR^2$, whereas a thin hoop has $I=MR^2$. This difference affects the pulley’s angular acceleration and the tensions on either side of the string.

## The Universal Mechanics Color Palette

Here is a standardized, high-contrast color-coding system optimized for classical mechanics diagrams. Using distinct colors for different physical quantities prevents your diagrams from becoming confusing when multiple vectors overlap.

 **Color Coding System**

| Vector Type           | Recommended Color    | Hex Code | Purpose & Best Practices                                                                                    |
|-----------------------|----------------------|----------|-------------------------------------------------------------------------------------------------------------|
| Displacement ($\Delta\vec{r}$) | Violet | #8A2BE2 | Shows the change in position from the initial to the final point. |
| Impulse ($\vec{J}$) | Electric Indigo | #4D00FF | Represents the change in momentum. Perfect for highlighting brief, high-force moments like a bat hitting a ball. |
| Net / Resultant Force | Crimson Red          | #CC0000  | Shows the final vector sum ($\vec{F}_{net}$). Use a thick line weight to make it dominant.                  |
| Component Forces      | Light / Rose Red     | #FF6666  | Used for resolved forces (like $F_{x}$ and $F_{y}$). Set to 50% opacity to sit quietly under the net force. |
| Applied Forces        | Royal Blue           | #0066CC  | Represents active external pushes, pulls, tensions ($\vec{T}$), or normal forces ($\vec{N}$).               |
| Resistive Forces      | Charcoal / Dark Grey | #4D4D4D  | Represents friction ($\vec{f}$) or air resistance. Keeps passive, opposing forces subtle.                   |
| Velocity              | Emerald Green        | #00994D  | Shows the direction of motion ($\vec{v}$). Easily distinguishes movement from the forces causing it.        |
| Acceleration          | Vibrant Orange       | #FF8000  | Shows acceleration ($\vec{a}$). Often drawn offset or floating next to the object, rather than attached.    |
| Momentum ($\vec{p}$) | Deep Navy Blue | #002266 | Represents linear momentum ($\vec{p} = m\vec{v}$). Since it shares the same direction as velocity, draw it parallel to your green velocity arrow, but slightly offset. |

### 💡 Visual Tip for Drawing Velocity vs. Momentum

Because momentum and velocity always point in the exact same direction, layering them directly on top of each other makes one disappear.
To show both clearly on a moving mass in Draw.io:

   1. Draw your Velocity arrow (#00994D Green) originating directly from the center of the object.
   2. Draw your Momentum arrow (#002266 Navy) slightly higher or lower, running perfectly parallel.
   3. Use a slightly thinner line weight (1.5pt) for the momentum arrow so it does not crowd the main velocity vector.

## 🛠️ How to Implement and Apply This Fast in Draw.io

Instead of manually coloring every arrow, use these two efficiency shortcuts:

### Shortcut 1: The Format Painter (Copy/Paste Styles)

- Style one arrow perfectly (e.g., Green, 2pt thickness, 50% opacity for velocity).
- Select that arrow and press Ctrl+Shift+C (or Cmd+Shift+C on Mac) to copy its style.
- Select any new arrow and press Ctrl+Shift+V (or Cmd+Shift+V on Mac) to paste the exact color and transparency instantly.

### Shortcut 2: Add Colors to Your Palette

- Select an arrow and click the Line Color box in the right-hand Format Panel.
- Type one of the hex codes above into the color picker box.
- Click the + icon in the "Remembered" colors section at the bottom to lock it into your workspace for the rest of your session.

Here is a high-contrast extension to your color-coding system, specifically selected for rotational mechanics. These colors are chosen to stand out clearly when overlaid on top of your linear forces (like applied force or gravity) and velocity arrows. [1]

## Rotational Mechanics Color Palette

| Vector / Quantity | Recommended Color  | Hex Code | Purpose & Best Practices                                                                                                                 |
|-------------------------------------------------|--------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------|
| Torque ($\vec{\tau}$)                           | Deep Purple        | #6600CC  | Represents rotational force. Use thick lines, often drawn as a curved arrow wrapping around a pivot point.                               |
| Angular Velocity ($\vec{\omega}$)               | Teal / Cyan        | #009999  | Shows the speed and direction of rotation. Complements the emerald green used for linear velocity.                                       |
| Angular Acceleration ($\vec{\alpha}$)           | Vibrant Orange     | #FF8000  | Shows the change in angular velocity; $\vec{\alpha} = \alpha_z\hat{k}$ points along the rotation axis for fixed-axis rotation.           |
| Angular Momentum ($\vec{L}$)                    | Magenta / Pink     | #CC0066  | Represents rotational momentum. Highly visible when drawn along the axis of rotation using the right-hand rule.                          |
| Centripetal / Radial Acceleration ($\vec{a}_c$) | Gold / Deep Yellow | #E6B800  | Points directly inward toward the center of the circular path. Distinct from the vibrant orange used for linear/tangential acceleration. |

## How to Use These for Rotational Visuals in Draw.io

Because rotational quantities are often represented as 3D concepts on a 2D canvas, use these styling tweaks to make them clear:

- The Right-Hand Rule (Linear Axes): When drawing $\vec{\omega}$ or $\vec{L}$ acting along a straight axis of rotation, make these arrows thicker (3pt) than your standard force lines to show they represent an entire rotational system.
- Curved Trajectories: For the curved arrows showing the direction of spin, use the Teal or Deep Purple with the Curve connector setting. Set the opacity to 70% if the curve passes over a solid body or mass.

## Lagrange's Equation

The core formula for **Lagrange's equation** (commonly referred to as the **Euler-Lagrange equation**) for a system described by a set of generalized coordinates $q_i$ is:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = 0$$

Or written equivalently:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) = \frac{\partial L}{\partial q_i}$$

### Component Breakdown

- **$L$ (The Lagrangian):** Defined as the difference between kinetic energy ($T$) and potential energy ($V$), $L = T - V$.

- **$q_i$:** The generalized coordinate representing the position of the system along the $i$-th degree of freedom (e.g., $x, y, z, \theta$).

- **$\dot{q}_i$:** The generalized velocity, defined as the time derivative of the generalized coordinate ($\dot{q}_i = \frac{dq_i}{dt}$).

- **$\frac{\partial L}{\partial \dot{q}_i}$:** The partial derivative of the Lagrangian with respect to generalized velocity (often called generalized momentum).

- **$\frac{\partial L}{\partial q_i}$:** The partial derivative of the Lagrangian with respect to the generalized coordinate (often corresponding to generalized force).

- **$t$:** Time.

### Extension (Non-Conservative Forces & Constraints)

If non-conservative forces $F$ or constraints $\eta$ are present in the system, the equation is generalized to:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) = \frac{\partial L}{\partial q_i} + F\frac{\partial \eta}{\partial q_i}$$

## Arc Length of functions

### Arc Length of a Function $y=f(x)$

For the graph $y=f(x)$ on the interval $a \le x \le b$, the <keyword id="kw_b1bd36303090bb4b622f6f93">arc length</keyword> is

$$
s=\int_a^b \sqrt{1+\left(f'(x)\right)^2}\,dx.
$$

**Conditions**

This formula applies when $f$ is differentiable on $[a,b]$ and $f'(x)$ is integrable.

### Arc Length of Parametric Functions

**1. Parametric arc length**

For a parametric curve

$$
x=x(t), \qquad y=y(t),
$$

the length over the parameter interval $t\in[a,b]$ is given by the <keyword id="kw_81f007bca8b1bc73351e873d">arc length formula</keyword>:

$$
s=\int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2}\,dt.
$$

This follows from

$$
ds=\sqrt{dx^2+dy^2}
$$

and the relations

$$
dx=\frac{dx}{dt}\,dt,
\qquad
dy=\frac{dy}{dt}\,dt.
$$

Therefore,

$$
\boxed{
s=\int_a^b
\sqrt{\left(x'(t)\right)^2+\left(y'(t)\right)^2}\,dt
}
$$

**2. Partial range of the curve**

If the desired portion corresponds to parameter values from $t=t_1$ to $t=t_2$, use

$$
\boxed{
s=\int_{t_1}^{t_2}
\sqrt{\left(x'(t)\right)^2+\left(y'(t)\right)^2}\,dt
}
$$

The direction of traversal does not affect the length, so one may use the smaller and larger parameter values as the limits.

**3. If the range is specified by $x$-values**

If the partial range is specified by $x=x_1$ to $x=x_2$, first find the corresponding parameter values:

$$
x(t_1)=x_1,
\qquad
x(t_2)=x_2.
$$

Then evaluate the same parametric arc length integral from $t_1$ to $t_2$. If $x(t)$ is one-to-one on the interval, this is direct. If not, split the curve into parameter intervals where the desired portion is traced exactly once.

----

[1] [https://maker.pro](https://maker.pro/custom/tutorial/what-is-torque-and-why-does-it-matter)

[2] [https://ilg.physics.ucsb.edu](https://ilg.physics.ucsb.edu/Courses/6/AL/?linkfile=lab4)

[3] [https://phys.libretexts.org](https://phys.libretexts.org/Courses/Georgia_State_University/GSU-TM-Physics_I_%282211%29/03%3A__Relative_and_Rotational_Motion/3.02%3A_Rotational_Variables)

[4] [https://www.vaia.com](https://www.vaia.com/en-us/textbooks/physics/21st-century-astronomy-4-edition/chapter-7/problem-30-how-does-the-law-of-conservation-of-angular-momen/)

[5] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/Angular_velocity)

[6] [https://ilg.physics.ucsb.edu](https://ilg.physics.ucsb.edu/Courses/6/AL/?linkfile=lab4)
