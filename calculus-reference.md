# Calculus Reference: Arc Length, Parametric Curves, and Geometry

## Arc Length of Parametric Curves

For a parametric curve:
$$x = x(t), \quad y = y(t)$$

the arc length over parameter interval $t \in [a,b]$ is:

$$
\boxed{s = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt}
$$

This formula follows from the differential arc length element:
$$ds = \sqrt{dx^2 + dy^2}$$

with the relations:
$$dx = \frac{dx}{dt}\,dt, \quad dy = \frac{dy}{dt}\,dt$$

### Conditions

This formula applies when $x(t)$ and $y(t)$ are differentiable on $[a,b]$ and their derivatives are integrable.

## Alternative Forms

### Using Prime Notation for Derivatives

$$
s = \int_a^b \sqrt{(x'(t))^2 + (y'(t))^2} \, dt
$$

### Specific Parameter Range $t_1 \le t \le t_2$

$$
s = \int_{t_1}^{t_2} \sqrt{(x'(t))^2 + (y'(t))^2} \, dt
$$

Note: The direction of traversal does not affect the arc length, so you may use the smaller and larger parameter values as the limits.

### When Range is Specified by $x$-Values

If the desired portion corresponds to $x = x_1$ to $x = x_2$:

1. Find the corresponding parameter values:
   $$x(t_1) = x_1, \quad x(t_2) = x_2$$

2. Evaluate the parametric arc length integral from $t_1$ to $t_2$:
   $$s = \int_{t_1}^{t_2} \sqrt{(x'(t))^2 + (y'(t))^2} \, dt$$

**Note:** If $x(t)$ is one-to-one on the interval, this is straightforward. If not, split the curve into parameter intervals where the desired portion is traced exactly once.

## Examples

### Example 1: Circle

For a circle of radius $R$:
$$x(t) = R\cos(t), \quad y(t) = R\sin(t), \quad t \in [0, 2\pi]$$

We have:
$$\frac{dx}{dt} = -R\sin(t), \quad \frac{dy}{dt} = R\cos(t)$$

$$s = \int_0^{2\pi} \sqrt{R^2\sin^2(t) + R^2\cos^2(t)} \, dt = \int_0^{2\pi} R \, dt = 2\pi R$$

This is the familiar circumference formula.

### Example 2: Semicircle from $(R, 0)$ to $(-R, 0)$

Same parametrization as above, but $t \in [0, \pi]$:

$$s = \int_0^{\pi} R \, dt = \pi R$$

This is half the circumference, as expected.

### Example 3: Straight Line Segment

For a line segment from $(x_1, y_1)$ to $(x_2, y_2)$:
$$x(t) = x_1 + t(x_2 - x_1), \quad y(t) = y_1 + t(y_2 - y_1), \quad t \in [0, 1]$$

We have:
$$\frac{dx}{dt} = x_2 - x_1, \quad \frac{dy}{dt} = y_2 - y_1$$

$$s = \int_0^1 \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2} \, dt = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$

This is the Euclidean distance formula, as expected.

## Arc Length in Physics Applications

### Circular Motion

For a particle moving in a circle of radius $r$ at angular velocity $\omega$:
$$\theta(t) = \omega t + \theta_0$$
$$s(t) = r\theta(t) = r(\omega t + \theta_0)$$

The instantaneous speed is:
$$v = \frac{ds}{dt} = r\omega$$

### Spiral Motion

For an Archimedean spiral:
$$r(\theta) = a\theta$$

In Cartesian coordinates:
$$x(\theta) = a\theta \cos(\theta), \quad y(\theta) = a\theta \sin(\theta)$$

The arc length from $\theta = 0$ to $\theta = \theta_1$ is:
$$s = \int_0^{\theta_1} \sqrt{(a\theta)^2 + a^2} \, d\theta$$

(This integral does not have a simple closed form for general $\theta_1$.)

## Related Topics

- **Curvature**: $\displaystyle \kappa = \frac{\vert\vec{r}' \times \vec{r}''\vert}{|\vec{r}'|^3}$ (for 2D or 3D curves)
- **Arc length parametrization**: Reparametrizing a curve by arc length $s$ instead of a parameter $t$
- **Surface area of revolution**: Extension of arc length to compute surface areas
- **Path integrals**: Line integrals along parametric curves in scalar and vector fields

----

## Plane Equations in Vector Form

### Setting up the Plane

A plane $\Pi$ is uniquely determined by a point $P_0$ on it and a nonzero
normal vector $\mathbf{n}$ perpendicular to it. Let $\mathbf{r}_0$ and
$\mathbf{r}$ be the position vectors of $P_0$ and of an arbitrary point $P$
on the plane.

### Point-Normal Equation

The vector $\overrightarrow{P_0P} = \mathbf{r} - \mathbf{r}_0$ lies in $\Pi$,
so it is perpendicular to $\mathbf{n}$. Using the dot product condition for
perpendicular vectors:

$$
\boxed{\mathbf{n}\cdot(\mathbf{r} - \mathbf{r}_0) = 0}
$$

Conversely, any point $P$ satisfying this equation lies in $\Pi$, so this
is the fundamental equation of the plane.

### Scalar (Cartesian) Form

Let $\mathbf{n} = a\,\mathbf{i} + b\,\mathbf{j} + c\,\mathbf{k}$,
$\mathbf{r} = x\,\mathbf{i} + y\,\mathbf{j} + z\,\mathbf{k}$, and
$\mathbf{r}_0 = x_0\,\mathbf{i} + y_0\,\mathbf{j} + z_0\,\mathbf{k}$.
Expanding the dot product gives:

$$
\begin{aligned}
a(x - x_0) + b(y - y_0) + c(z - z_0) &= 0 \\
ax + by + cz &= d,
\quad \text{where} \quad d = ax_0 + by_0 + cz_0
\end{aligned}
$$

This is the standard Cartesian equation of a plane.

### Parametric Vector Form

If the plane is specified by two non-parallel direction vectors
$\mathbf{u}$ and $\mathbf{v}$ lying in $\Pi$, a normal can be taken as
$\mathbf{n} = \mathbf{u} \times \mathbf{v}$, which is perpendicular to
both. Since $\mathbf{r} - \mathbf{r}_0$ is perpendicular to $\mathbf{n}$,
it lies in the plane spanned by $\mathbf{u}$ and $\mathbf{v}$, so it can
be written as a linear combination of them:

$$
\mathbf{r} - \mathbf{r}_0 = s\,\mathbf{u} + t\,\mathbf{v}
$$

Hence the parametric equation is:

$$
\mathbf{r} = \mathbf{r}_0 + s\,\mathbf{u} + t\,\mathbf{v},
\quad s, t \in \mathbb{R}
$$

### Summary of Plane Equation Forms

| Form | Equation | Parameters |
| --- | --- | --- |
| Point-Normal | $\mathbf{n}\cdot(\mathbf{r} - \mathbf{r}_0) = 0$ | Normal vector $\mathbf{n}$, point $P_0$ |
| Scalar | $ax + by + cz = d$ | Coefficients $a, b, c$ from $\mathbf{n}$, constant $d$ |
| Parametric | $\mathbf{r} = \mathbf{r}_0 + s\,\mathbf{u} + t\,\mathbf{v}$ | Point $P_0$, direction vectors $\mathbf{u}, \mathbf{v}$ |

----

## Line Equations in Vector Form

### Setting up the Line

A line $L$ is uniquely determined by a point $P_0$ on it and a nonzero
direction vector $\mathbf{d}$ parallel to it. Let $\mathbf{r}_0$ and
$\mathbf{r}$ be the position vectors of $P_0$ and of an arbitrary point
$P$ on the line.

### Parametric Vector Form

The most natural form for a line is the parametric form. A point $P$ with
position vector $\mathbf{r}$ lies on the line if and only if:

$$
\boxed{\mathbf{r} = \mathbf{r}_0 + t\,\mathbf{d}, \quad t \in \mathbb{R}}
$$

where $\mathbf{d}$ is the direction vector and $t$ is the parameter. The
point $P_0$ corresponds to $t = 0$.

### Symmetric (Cartesian) Form

Let $\mathbf{d} = a\,\mathbf{i} + b\,\mathbf{j} + c\,\mathbf{k}$ with
$a, b, c \neq 0$, and let $\mathbf{r}_0 = x_0\,\mathbf{i} + y_0\,\mathbf{j} +
z_0\,\mathbf{k}$. From the parametric form:

$$
\begin{aligned}
x &= x_0 + at \\
y &= y_0 + bt \\
z &= z_0 + ct
\end{aligned}
$$

Solving for $t$ in each equation and equating:

$$
\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}
$$

This is the symmetric (or canonical) form of the line. It works when all
direction components are nonzero.

### Two-Point Form

If the line passes through two distinct points $P_1$ and $P_2$ with
position vectors $\mathbf{r}_1$ and $\mathbf{r}_2$, the direction vector
is:

$$
\mathbf{d} = \mathbf{r}_2 - \mathbf{r}_1
$$

and the parametric equation becomes:

$$
\mathbf{r} = \mathbf{r}_1 + t(\mathbf{r}_2 - \mathbf{r}_1),
\quad t \in \mathbb{R}
$$

When $t = 0$, we are at $P_1$; when $t = 1$, we are at $P_2$. The line
segment between them corresponds to $0 \le t \le 1$.

### Scalar Form (Implicit)

A line in 3D can also be written as the intersection of two planes:

$$
\begin{aligned}
a_1 x + b_1 y + c_1 z &= d_1 \\
a_2 x + b_2 y + c_2 z &= d_2
\end{aligned}
$$

The direction vector of the line is perpendicular to both normal vectors
$\mathbf{n}_1 = (a_1, b_1, c_1)$ and $\mathbf{n}_2 = (a_2, b_2, c_2)$, so:

$$
\mathbf{d} = \mathbf{n}_1 \times \mathbf{n}_2
$$

### Summary of Line Equation Forms

| Form | Equation | Parameters |
| --- | --- | --- |
| Parametric | $\mathbf{r} = \mathbf{r}_0 + t\,\mathbf{d}$ | Point $P_0$, direction $\mathbf{d}$, parameter $t$ |
| Symmetric | $\displaystyle \frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}$ | Point $(x_0, y_0, z_0)$, direction $(a, b, c)$ |
| Two-Point | $\mathbf{r} = \mathbf{r}_1 + t(\mathbf{r}_2 - \mathbf{r}_1)$ | Two points $P_1, P_2$ on the line |
| Implicit | $\begin{aligned} a_1 x + b_1 y + c_1 z &= d_1 \\ a_2 x + b_2 y + c_2 z &= d_2 \end{aligned}$ | Two plane equations |

----

## Related Topics

- **Distance from point to line**: 
  $\displaystyle \text{dist} = \frac{\vert(\mathbf{r}_P - \mathbf{r}_0) 
  \times \mathbf{d}\vert}{|\mathbf{d}|}$
- **Distance between two skew lines**: Using dot product of relative
  position and cross product of directions
- **Line-plane intersection**: Finding where a parametric line meets
  a plane
- **Angle between lines**: Using the dot product of direction vectors
- **Projection of point onto line**: Finding the closest point on the
  line to a given point
- **Distance from point to plane**: 
  $\displaystyle \text{dist} = \frac{\vert\mathbf{n}\cdot(\mathbf{r}_P - 
  \mathbf{r}_0)\vert}{|\mathbf{n}|}$
- **Surfaces of revolution**: Parametric surfaces extending geometry

---

## References

- Stewart, J. *Calculus* (8th ed.). Cengage Learning.
- https://en.wikipedia.org/wiki/Arc_length
- https://mathworld.wolfram.com/ArcLength.html
- https://en.wikipedia.org/wiki/Plane_(geometry)
- https://mathworld.wolfram.com/Plane.html
- https://en.wikipedia.org/wiki/Line_(geometry)
- https://mathworld.wolfram.com/Line.html
