# Physics Notes: Classical Mechanics

## Kinematic Motion

### Fundamental Relations

$$
\boxed{
    \begin{aligned}
        \frac{d v}{d t} &= a(t) \\
        v_f - v_i &= \int^{t_1}_{t_0} a \, dt
    \end{aligned}
}
$$

### Acceleration as a Function of Velocity

$$
\boxed{
    \begin{aligned}
        a(v) &= \frac{d v}{d t} \\
        a(v) &= \frac{d v}{d x} \frac{d x}{d t} \\
        a(v) &= v \frac{d v}{d x} \\
        dx &= \frac{v \, dv}{a(v)} \\
        \int_{x_0}^{x_1} dx &= \int_{v_0}^{v_1} \frac{v \, dv}{a(v)} \quad \Rightarrow \quad
        x_f - x_i = \int_{v_i}^{v_f} \frac{v \, dv}{a(v)}
    \end{aligned}
}
$$

### Acceleration as a Function of Position

$$
\boxed{
    \begin{aligned}
        a(x) &= \frac{d v}{d t} \\
        a(x) &= \frac{d v}{d x} \frac{d x}{d t} \\
        a(x) &= v \frac{d v}{d x} \\
        a(x) \, dx &= v \, dv \\
        \int_{x_i}^{x_f} a(x) \, dx &= \int_{v_i}^{v_f} v \, dv \quad \Rightarrow \quad
        v_f^2 - v_i^2 = 2 \int_{x_0}^{x_1} a(x) \, dx
    \end{aligned}
}
$$

----

## Uniform Circular Motion

### Core Formulas

| Quantity | Symbol | Formula | Units |
| --- | --- | --- | --- |
| Period | $T$ | $\displaystyle T = \frac{2\pi r}{v} = \frac{2\pi}{\omega} = \frac{1}{f}$ | s |
| Frequency | $f$ | $\displaystyle f = \frac{1}{T} = \frac{\omega}{2\pi}$ | Hz |
| Angular velocity | $\omega$ | $\displaystyle \omega = \frac{d\theta}{dt} = \frac{2\pi}{T} = 2\pi f = \frac{v}{r}$ | rad/s |
| Angular position | $\theta$ | $\displaystyle \theta(t) = \theta_0 + \omega t$ | rad |
| Arc length | $s$ | $\displaystyle s = r\theta$ | m |
| Tangential speed | $v$ | $\displaystyle v = \omega r = \frac{2\pi r}{T}$ | m/s |
| Centripetal acceleration | $a_c$ | $\displaystyle a_c = \frac{v^2}{r} = \omega^2 r = v\omega$ | m/s² |
| Centripetal force | $F_c$ | $\displaystyle F_c = \frac{m v^2}{r} = m\omega^2 r$ | N |

### Vector Form

| Quantity | Formula |
| --- | --- |
| Position | $\displaystyle \vec{r}(t) = r\left[\cos(\omega t + \theta_0)\,\hat{i} + \sin(\omega t + \theta_0)\,\hat{j}\right]$ |
| Velocity | $\displaystyle \vec{v}(t) = r\omega\left[-\sin(\omega t + \theta_0)\,\hat{i} + \cos(\omega t + \theta_0)\,\hat{j}\right] = \vec{\omega}\times\vec{r}$ |
| Acceleration | $\displaystyle \vec{a}(t) = -r\omega^2\left[\cos(\omega t + \theta_0)\,\hat{i} + \sin(\omega t + \theta_0)\,\hat{j}\right] = -\omega^2\vec{r}$ |

### Key Properties

- $\displaystyle \vec{v}$ is tangent to the circle; $\displaystyle \vec{a}$ points toward the center, so $\displaystyle \vec{v} \cdot \vec{a} = 0$
- Speed is constant, but velocity direction changes continuously → non-zero acceleration
- Centripetal force is the *net* inward force (tension, gravity, friction, etc.), not a separate force

### Lagrangian Form

For motion on a circle of constant radius $R$:

| Quantity | Formula |
| --- | --- |
| Lagrangian | $\displaystyle L = \tfrac{1}{2} m R^2 \dot{\theta}^2 - V(\theta)$ |
| Equation of motion | $\displaystyle mR^2\ddot{\theta} = \tau \quad \text{or} \quad \ddot{\theta} = \frac{\tau}{mR^2}$ |

----

## Rotational Mechanics

### Rotational Kinematics

| Concept | Formula |
| --- | --- |
| Angular Velocity Vector | $\displaystyle \vec{\omega} = \frac{d\theta}{dt} \hat{k} = \omega_z \hat{k}$ |
| Angular Acceleration Vector | $\displaystyle \vec{\alpha} = \frac{d^2\theta}{dt^2} \hat{k} = \alpha_z \hat{k}$ |
| Tangential Velocity | $\displaystyle v_{\theta} = r \omega_z$ |
| Tangential Acceleration | $\displaystyle a_{\theta} = r \alpha_z$ |
| Centripetal Acceleration | $\displaystyle a_{r} = -r \omega_z^2$ |

### Moment of Inertia

| Concept | Formula |
| --- | --- |
| Definition (continuous) | $\displaystyle I = \int_{\text{body}} r^2 \, dm$ |
| Definition (discrete) | $\displaystyle I = \sum_i m_i r_i^2$ |
| Rotational Kinetic Energy | $\displaystyle K_{\text{rot}} = \frac{1}{2} I \omega^2$ |

#### Common Moments of Inertia (about center of mass or specified axis)

| Object | Axis | Moment of Inertia |
| --- | --- | --- |
| Point mass | Distance $r$ from axis | $\displaystyle I = Mr^2$ |
| Thin hoop or ring | Through center, perpendicular to plane | $\displaystyle I = MR^2$ |
| Solid disc or cylinder | Through center, perpendicular to plane / longitudinal | $\displaystyle I = \frac{1}{2}MR^2$ |
| Hollow cylinder (thin-walled) | Longitudinal axis | $\displaystyle I = MR^2$ |
| Solid sphere | Through center | $\displaystyle I = \frac{2}{5}MR^2$ |
| Thin spherical shell | Through center | $\displaystyle I = \frac{2}{3}MR^2$ |
| Thin rod | Through center, perpendicular to rod | $\displaystyle I = \frac{1}{12}ML^2$ |
| Thin rod | Through one end, perpendicular to rod | $\displaystyle I = \frac{1}{3}ML^2$ |
| Rectangular plate | Through center, perpendicular to plate | $\displaystyle I = \frac{1}{12}M(a^2+b^2)$ |
| Annular disc (ring with inner/outer radius) | Through center, perpendicular to plane | $\displaystyle I = \frac{1}{2}M(R_o^2+R_i^2)$ |

### Parallel Axis Theorem

If $I_{\text{cm}}$ is the moment of inertia about an axis through the center of mass, then the moment of inertia about a parallel axis at distance $d$ away is:

$$
\boxed{
I = I_{\text{cm}} + Md^2
}
$$

#### Examples

| Object | Calculation | Result |
| --- | --- | --- |
| Thin rod (about one end) | $\displaystyle I = \frac{1}{12}ML^2 + M\left(\frac{L}{2}\right)^2$ | $\displaystyle I = \frac{1}{3}ML^2$ |
| Disc (about rim, perpendicular axis) | $\displaystyle I = \frac{1}{2}MR^2 + MR^2$ | $\displaystyle I = \frac{3}{2}MR^2$ |

### Vector Cross Product

| Concept | Formula |
| --- | --- |
| Magnitude | $\displaystyle \vert\vec{A} \times \vec{B}\vert = \vert\vec{A}\vert \vert\vec{B}\vert \sin\theta$ |
| Cartesian components | $\displaystyle \vec{A} \times \vec{B} = (A_y B_z - A_z B_y)\hat{i} + (A_z B_x - A_x B_z)\hat{j} + (A_x B_y - A_y B_x)\hat{k}$ |
| Cylindrical basis | $\displaystyle \hat{r} \times \hat{\theta} = \hat{k}, \quad \hat{\theta} \times \hat{k} = \hat{r}, \quad \hat{k} \times \hat{r} = \hat{\theta}$ |

### Torque

| Concept | Formula |
| --- | --- |
| Torque vector about point $S$ | $\displaystyle \vec{\tau}_S = \vec{r}_{S, P} \times \vec{F}_P$ |
| Torque magnitude | $\displaystyle \tau_S = r F \sin\theta = r_{\perp} F = r F_{\perp}$ |
| Moment arm | $\displaystyle r_{\perp} = r \sin\theta$ |
| Gravitational torque | $\displaystyle \vec{\tau}_O = \vec{R}_{\text{cm}} \times M\vec{g}$ |

### Rotational Dynamics

| Concept | Formula |
| --- | --- |
| Newton's 2nd Law (rotational) | $\displaystyle \tau_z^{\text{ext}} = I \alpha_z$ |
| Angular momentum | $\displaystyle \vec{L} = I \vec{\omega}$ |
| Rotational impulse-momentum | $\displaystyle \vec{\tau} \, \Delta t = \Delta \vec{L}$ |

### Rotational Work, Energy, and Power

| Concept | Formula |
| --- | --- |
| Infinitesimal work | $\displaystyle dW = \tau_z \, d\theta$ |
| Total work | $\displaystyle W = \int_{\theta_i}^{\theta_f} \tau_z \, d\theta$ |
| Work-energy theorem | $\displaystyle W = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2 = \Delta K_{\text{rot}}$ |
| Power | $\displaystyle P = \frac{dW}{dt} = \tau_z \omega_z$ |

----

## See Also

- **[color-schemes.md](color-schemes.md)** — Visualization conventions and diagramming color palettes for classical mechanics
- **[calculus-reference.md](calculus-reference.md)** — Arc length, parametric curves, and related calculus topics

## References

[1] https://maker.pro/custom/tutorial/what-is-torque-and-why-does-it-matter

[2] https://ilg.physics.ucsb.edu/Courses/6/AL/?linkfile=lab4

[3] https://phys.libretexts.org/Courses/Georgia_State_University/GSU-TM-Physics_I_%282211%29/03%3A__Relative_and_Rotational_Motion/3.02%3A_Rotational_Variables

[4] https://www.vaia.com/en-us/textbooks/physics/21st-century-astronomy-4-edition/chapter-7/problem-30-how-does-the-law-of-conservation-of-angular-momen/

[5] https://en.wikipedia.org/wiki/Angular_velocity
