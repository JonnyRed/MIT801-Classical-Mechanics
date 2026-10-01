# Rotational Dynamics Reference Sheet: Torque & Moment of Inertia

This reference sheet covers the definitions, physical principles, geometric theorems, and mathematical relationships governing **Torque** ($\vec{\tau}$) and **Moment of Inertia** ($I$) in fixed-axis rotational dynamics.

---

1. Torque ($\vec{\tau}$)

1.1 Vector Definition and Cross Product
Torque measures the twisting or rotational effect of an applied force about a specific pivot point $S$ [110, 120]. For a force $\vec{F}_P$ applied at point $P$, with position vector $\vec{r}_{S,P}$ drawn from pivot $S$ to $P$, torque is defined as the vector cross product [23, 121]:
$$\vec{\tau}_S = \vec{r}_{S,P} \times \vec{F}_P$$

* **Magnitude**:
  $$\tau_S = |\vec{r}_{S,P}| |\vec{F}_P| \sin\theta = r F \sin\theta$$
  where $\theta$ is the angle between $\vec{r}_{S,P}$ and $\vec{F}_P$ ($0 \le \theta \le \pi$) [121, 122].
* **Equivalent Interpretations**:
  1. **Moment Arm ($r_\perp$)**: $\tau_S = r_\perp F$, where $r_\perp = r \sin\theta$ is the perpendicular distance from the pivot $S$ to the line of action of the force [23, 123, 124].
  2. **Perpendicular Force ($F_\perp$)**: $\tau_S = r F_\perp$, where $F_\perp = F \sin\theta$ is the component of force perpendicular to the position vector $\vec{r}_{S,P}$ [23, 123].

1.2 Sign Conventions & Direction (Right-Hand Rule)

* The vector direction of $\vec{\tau}_S$ is perpendicular to the plane formed by $\vec{r}_{S,P}$ and $\vec{F}_P$, given by the **Right-Hand Rule** [21, 122].
* For 2D coplanar motion about the $z$-axis:
  * **Counterclockwise (CCW)** torque points in the $+\hat{k}$ direction ($\tau_z > 0$) [71, 126, 128].
  * **Clockwise (CW)** torque points in the $-\hat{k}$ direction ($\tau_z < 0$) [71, 128].

1.3 Internal Torque Cancellation
For a system of particles or continuous rigid body, internal forces occur in equal and opposite pairs according to Newton's Third Law ($\vec{F}_{j,i} = -\vec{F}_{i,j}$) [31, 143]. Because internal forces act along the straight line connecting the mass elements, their relative position vector $\vec{r}_{S,i} - \vec{r}_{S,j}$ is collinear with $\vec{F}_{j,i}$ [31, 144]. Consequently:
$$(\vec{r}_{S,i} - \vec{r}_{S,j}) \times \vec{F}_{j,i} = \vec{0}$$
**Internal torques cancel out in pairs**, meaning net rotational motion is governed solely by **external torques** [31, 144, 146]:
$$\vec{\tau}_S^{\text{net}} = \vec{\tau}_S^{\text{ext}}$$

---

2. Moment of Inertia ($I$)

2.1 Definition and Physical Meaning
Moment of Inertia $I_S$ is the rotational analog to mass [15, 18]. It quantifies an object's resistance to angular acceleration about a specified rotation axis passing through point $S$ [17, 18, 30]:

* **Discrete Mass System**:
  $$I_S = \sum_{j=1}^N \Delta m_j r_{\perp, j}^2$$
* **Continuous Body**:
  $$I_S = \int_{\text{body}} r_\perp^2 \, dm$$
  where $r_\perp$ is the perpendicular distance from the mass element $dm$ to the axis of rotation [8, 18].
* **SI Units**: $\text{kg} \cdot \text{m}^2$ [78].

*Key Insight*: Unlike translational mass (which is constant), $I$ depends not only on total mass, but also on **how that mass is distributed** relative to the rotation axis [18, 19]. Moving mass farther from the axis dramatically increases $I$ due to the $r_\perp^2$ factor [18, 19].

---

2.2 Moments of Inertia for Common Standard Shapes

1. **Thin Uniform Rod (length $L$, mass $m$)**:
   * About center of mass: $I_{\text{cm}} = \frac{1}{12} m L^2$ [10, 81]
   * About one end: $I_{\text{end}} = \frac{1}{3} m L^2$ [12, 89]

2. **Thin Uniform Disc or Solid Cylinder (radius $R$, mass $m$)**:
   * About central axis perpendicular to disc: $I_{\text{cm}} = \frac{1}{2} m R^2$ [11, 85]

3. **Solid Uniform Sphere (radius $R$, mass $m$)**:
   * About any central axis: $I_{\text{cm}} = \frac{2}{5} m R^2$ [3]

---

2.3 Parallel Axis Theorem

The **Parallel Axis Theorem** relates the moment of inertia $I_S$ about any axis passing through point $S$ to the moment of inertia $I_{\text{cm}}$ about a parallel axis passing through the body's center of mass [4, 88]:
$$I_S = I_{\text{cm}} + m d_{S, \text{cm}}^2$$
where:

* $I_{\text{cm}}$ is the moment of inertia about the parallel axis through the center of mass [4, 87].
* $m$ is the total mass of the object [4, 88].
* $d_{S, \text{cm}}$ is the perpendicular separation distance between the two parallel axes [4, 87, 88].

*Note*: $I_{\text{cm}}$ is the **minimum possible** moment of inertia for any family of parallel axes [4, 88].

---

3. The Rotational Equation of Motion

Combining torque and moment of inertia yields the rotational equivalent of Newton's Second Law ($\vec{F} = m\vec{a}$) for fixed-axis rotation [15, 30, 146]:
$$\tau_{S, z}^{\text{ext}} = I_S \alpha_z$$
where:

* $\tau_{S, z}^{\text{ext}}$ is the net external torque component along the $z$-axis of rotation [30, 141, 146].
* $I_S$ is the moment of inertia about axis $S$ [30, 141].
* $\alpha_z = \frac{d\omega_z}{dt} = \frac{d^2\theta}{dt^2}$ is the $z$-component of angular acceleration [2, 70, 141].

---

4. Rotational Energy, Work, and Power

* **Rotational Kinetic Energy**:
  $$K_{\text{rot}} = \frac{1}{2} I_S \omega_z^2$$
* **Rotational Work**:
  $$W_{\text{rot}} = \int_{\theta_i}^{\theta_f} \tau_{S, z} \, d\theta$$
* **Work-Kinetic Energy Theorem**:
  $$W_{\text{rot}} = \frac{1}{2} I_S \omega_{z, f}^2 - \frac{1}{2} I_S \omega_{z, i}^2 = \Delta K_{\text{rot}}$$
* **Rotational Power**:
  $$P_{\text{rot}} = \frac{dW_{\text{rot}}}{dt} = \tau_{S, z} \omega_z$$
