# Chapter 19: Angular Momentum — Worked Examples

## Example 19.1: Angular Momentum — Constant Velocity

**Problem:** A particle of mass $m = 2.0\text{ kg}$ moves with uniform velocity $\vec{v} = 3.0\hat{i} + 3.0\hat{j}\text{ m}\cdot\text{s}^{-1}$. At time $t$, it passes through the point $(2.0\text{ m}, 3.0\text{ m})$. Find the direction and magnitude of the angular momentum relative to the origin $S$.

**Solution**

| Quantity | Expression |
| --- | --- |
| Position | $\displaystyle \vec{r}_S = 2.0\hat{i} + 3.0\hat{j}\text{ m}$ |
| Momentum | $\displaystyle \vec{p} = m\vec{v} = 2.0(3.0\hat{i} + 3.0\hat{j}) = 6.0\hat{i} + 6.0\hat{j}\text{ kg}\cdot\text{m}\cdot\text{s}^{-1}$ |

Cross product:

$$
\begin{aligned}
\vec{L}_S &= \vec{r}_S \times \vec{p} \\
&= (2.0\hat{i} + 3.0\hat{j}) \times (6.0\hat{i} + 6.0\hat{j}) \\
&= -6.0\hat{k}\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-1}
\end{aligned}
$$

**Result:** Magnitude is $6.0\text{ kg}\cdot\text{m}^2\cdot\text{s}^{-1}$ in the $-\hat{k}$ direction.

## Example 19.2: Angular Momentum and Circular Motion

**Problem:** A particle of mass $m$ moves in a circle of radius $R$ in the $x$-$y$ plane with angular velocity $\vec{\omega} = \omega_z \hat{k}$ ($\omega_z > 0$). Find $\vec{L}_S$ relative to the center of the orbit $S$.

**Solution**

| Quantity | Expression |
| --- | --- |
| Velocity | $\displaystyle \vec{v} = R\omega_z \hat{\theta}$ |
| Position | $\displaystyle \vec{r}_S = R\hat{r}$ |

Cross product:

$$
\vec{L}_S = \vec{r}_S \times m\vec{v} = R\hat{r} \times m R \omega_z \hat{\theta} = m R^2 \omega_z \hat{k}
$$

**Result:** $\vec{L}_S = I_S \omega_z \hat{k}$, where $I_S = m R^2$ is the moment of inertia about the $z$-axis.

## Example 19.3: Angular Momentum About a Point Along the Central Axis

**Problem:** A particle of mass $m$ moves in a circle of radius $R$ with angular velocity $\vec{\omega} = \omega_z \hat{k}$ at a height $h$ above the $x$-$y$ plane. Find $\vec{L}_S$ relative to the origin $S$ on the $z$-axis.

**Solution**

| Quantity | Expression |
| --- | --- |
| Position | $\displaystyle \vec{r}_S = R\hat{r} + h\hat{k}$ |
| Momentum | $\displaystyle \vec{p} = m R \omega_z \hat{\theta}$ |

Cross product:

$$
\vec{L}_S = (R\hat{r} + h\hat{k}) \times m R \omega_z \hat{\theta} = m R^2 \omega_z \hat{k} - h m R \omega_z \hat{r}
$$

Magnitude: $L_S = m R \omega_z \sqrt{R^2 + h^2}$

**Result:** The magnitude is constant, but the vector direction sweeps out a cone around the $z$-axis as the particle rotates. The $z$-component $L_{S,z} = m R^2 \omega_z$ remains independent of height $h$.

## Example 19.4: Meteor Flyby of Earth

**Problem:** A meteor of mass $m$ approaches Earth ($M_E, R_E$) starting far away with speed $v_i$ at impact parameter $h$. At nearest approach, it just grazes Earth. Find distance $h$.

**Solution**

Torque about Earth's center is zero ($\vec{r} \parallel \vec{F}_G$), so angular momentum is conserved:

$$
L_{S,i} = m v_i h = m v_p R_E = L_{S,E} \implies v_p = \frac{v_i h}{R_E}
$$

Conservation of mechanical energy:

$$
\frac{1}{2} m v_i^2 = \frac{1}{2} m v_p^2 - \frac{G m M_E}{R_E}
$$

**Result:** 
$$h = R_E \sqrt{1 + \frac{2 G M_E}{v_i^2 R_E}}$$

## Example 19.5: Angular Momentum of Two Particles in Circular Motion

**Problem:** Two identical masses $m$ are located on opposite sides of a circle of radius $R$ at height $h$ above the $x$-$y$ plane, rotating with $\vec{\omega} = \omega_z \hat{k}$. Find $\vec{L}_S$ about origin $S$.

**Solution**

| Particle | Angular momentum |
| --- | --- |
| 1 | $\displaystyle \vec{L}_{S,1} = m R^2 \omega_z \hat{k} - h m R \omega_z \hat{r}_1$ |
| 2 | $\displaystyle \vec{L}_{S,2} = m R^2 \omega_z \hat{k} - h m R \omega_z \hat{r}_2$ |

Since $\hat{r}_1 = -\hat{r}_2$, radial terms cancel upon addition:

$$
\vec{L}_S = \vec{L}_{S,1} + \vec{L}_{S,2} = 2 m R^2 \omega_z \hat{k}
$$

**Result:** $\vec{L}_S = I_S \omega_z \hat{k}$, pointing along the rotation axis because of the symmetric mass distribution.

## Example 19.6 (A): Angular Momentum About Different Points

**Problem:** Relate the total angular momentum of an $N$-particle system about point $A$ ($\vec{L}_A$) to that about point $B$ ($\vec{L}_B$).

**Solution**

Position relation: $\vec{r}_{A,j} = \vec{r}_{B,j} + \vec{r}_{A,B}$

Summing individual angular momenta:

$$
\begin{aligned}
\vec{L}_A &= \sum_j \vec{r}_{B,j} \times m_j \vec{v}_j
    + \vec{r}_{A,B} \times \sum_j m_j \vec{v}_j \\
&= \vec{L}_B + \vec{r}_{A,B} \times \vec{p}_{\text{sys}}
\end{aligned}
$$

**Result:** $\vec{L}_A = \vec{L}_B + \vec{r}_{A,B} \times \vec{p}_{\text{sys}}$. If $\vec{p}_{\text{sys}} = \vec{0}$ (such as in the center of mass frame), $\vec{L}_A = \vec{L}_B$.

## Example 19.6 (B): Circular Ring

**Problem:** A circular ring of radius $R$ and mass $M$ rotates about the $z$-axis at height $h$ above the $x$-$y$ plane with $\vec{\omega} = \omega_z \hat{k}$. Find $\vec{L}_S$ at any point $S$ on the central axis.

**Solution**

By grouping infinitesimal mass elements into symmetric diametrically opposed pairs $m_{\text{pair}}$, non-$z$ components cancel:

$$
\vec{L}_{\text{pair}} = m_{\text{pair}} R^2 \omega_z \hat{k}
$$

Integrating/summing over all pairs:

$$
\vec{L}_S = M R^2 \omega_z \hat{k}
$$

**Result:** $\vec{L}_S = I_S \omega_z \hat{k}$, where $I_S = M R^2$.

## Example 19.7: Collision Between a Pivoted Rod and an Object

**Problem:** Mass $m_1$ moving at $v_i$ strikes a uniform hanging rod ($m_2, l$, pivoted at top). Immediately after, $m_1$ moves at $v_i/2$.

(a) Find $v_i$ so the rod just touches the ceiling ($v_f = 0$ at top of swing).

(b) Find ratio $m_2/m_1$ for the collision to be elastic.

**Solution**

Angular Momentum Balance about Pivot:

$$
\begin{aligned}
m_1 v_i l &= m_1 \left(\frac{v_i}{2}\right) l + I_S \omega_a \\
\omega_a &= \frac{3 m_1 v_i}{2 m_2 l}, \qquad I_S = \frac{1}{3} m_2 l^2
\end{aligned}
$$

Energy Conservation during Swing (State $a$ to $f$):

$$
\frac{1}{2} I_S \omega_a^2 = m_2 g \left(\frac{l}{2}\right) \implies \frac{3 m_1^2 v_i^2}{8 m_2} = m_2 g \left(\frac{l}{2}\right)
$$

Elastic Collision Condition: $\frac{1}{2} m_1 v_i^2 = \frac{1}{2} m_1 \left(\frac{v_i}{2}\right)^2 + \frac{1}{2} I_S \omega_a^2$

**Results**

- (a) $\displaystyle v_i = \frac{m_2}{m_1} \sqrt{\frac{4 g l}{3}}$
- (b) $\displaystyle \frac{m_2}{m_1} = 1$

## Example 19.8: Angular Impulse on a Steel Washer

**Problem:** A motor and washer ($I_0$) spin at $\omega_0$. Power shuts off at $t=0$, slowing them down due to frictional torque $\tau_f$. At $t_a$ (speed $\omega_a$), a second washer ($I_w$) is dropped on top.

**Solution**

(a) Angular acceleration during initial coasting: $\alpha_1 = \frac{\omega_a - \omega_0}{\Delta t_1} < 0$. Frictional torque: $\tau_f = -I_0 \alpha_1$.

(b) Instantaneous collision ($\Delta t_{\text{int}} \approx 0$):

$$
0 = \Delta L_z \implies (I_0 + I_w)\omega_b = I_0 \omega_a \implies \omega_b = \frac{I_0}{I_0 + I_w} \omega_a
$$

(c) Non-instantaneous collision over interval $\Delta t_{\text{int}}$: Frictional angular impulse is:

$$
J_z = -\tau_f \Delta t_{\text{int}} = I_0 (\omega_a - \omega_0) \frac{\Delta t_{\text{int}}}{\Delta t_1}
$$

(d) Post-collision speed with friction:

$$
\begin{aligned}
J_z &= \Delta L_z = (I_0 + I_w)\omega_b - I_0 \omega_a \\
\omega_b &= \frac{I_0}{I_0 + I_w} \left( (\omega_a - \omega_0)\frac{\Delta t_{\text{int}}}{\Delta t_1} + \omega_a \right)
\end{aligned}
$$

(e) Post-collision deceleration:

$$
\alpha_2 = \frac{-\omega_b}{\Delta t_2}
$$
