# Rotational Motion Reference Sheet

This reference sheet covers angular velocity, torque, and moment of inertia — the core definitions, physical principles, geometric theorems, and mathematical relationships governing fixed-axis rotational kinematics and dynamics.

---

## 1. Angular Velocity and $\omega_z = \frac{d\theta}{dt}$

The formula **$\omega_z = \frac{d\theta}{dt}$** defines the **$z$-component of the angular velocity vector** for a rigid body undergoing fixed-axis rotation. In the broader framework of rotational kinematics and dynamics, this relation serves as the fundamental link between an object's changing angular position, its vector representation of rotation, its linear velocity at individual points, and its overall rotational energy.

### 1.1 Component vs. Vector Representation

* **The Scalar Component ($\omega_z$)**: The quantity $\omega_z \equiv \frac{d\theta}{dt}$ is the time derivative of the angle $\theta$ that describes the rotational position of a reference line in the plane of rotation. It measures the rate at which this angle changes over time.
* **The Angular Velocity Vector ($\vec{\omega}$)**: Angular velocity is fundamentally a vector quantity. For rotation about a fixed $z$-axis, the angular velocity vector is directed along the axis of rotation perpendicular to the plane of motion:
  $$\vec{\omega} = \frac{d\theta}{dt} \hat{k} = \omega_z \hat{k}$$
  where $\hat{k}$ is the unit vector along the $z$-axis.

### 1.2 Sign Convention and Direction (Right-Hand Rule)

Because $\omega_z$ is an algebraic component, it can be positive, zero, or negative:

* **Counterclockwise Rotation**: Using a standard right-handed coordinate system, if the object rotates counterclockwise when viewed from above the plane of rotation, $\theta$ increases with time ($\omega_z > 0$) and $\vec{\omega}$ points in the **$+\hat{k}$ direction**.
* **Clockwise Rotation**: If the object rotates clockwise, $\theta$ decreases with time ($\omega_z < 0$) and $\vec{\omega}$ points in the **$-\hat{k}$ direction**.
* **Right-Hand Rule**: The vector direction is established by curling the fingers of the right hand in the direction of rotation; the extended right thumb points in the direction of $\vec{\omega}$.

### 1.3 Uniformity Across a Rigid Body

A defining property of a **rigid body** in fixed-axis rotation is that **every single mass element or point in the body shares the exact same angular velocity $\omega_z$** at any instant. If different parts of the object possessed different angular velocities, mass elements would catch up to or pass one another, which would violate the rigid-body condition that inter-point distances remain fixed.

### 1.4 Broader Context in Kinematics and Dynamics

Within the broader framework of classical mechanics, $\omega_z$ connects to several critical concepts:

* **Tangential Velocity**: A mass element located at a distance $r_i$ from the axis of rotation moves in a circle with a tangential velocity component given by:
  $$v_{\theta, i} = r_i \omega_z$$
  Points farther from the axis travel faster linearly, even though all points share the same $\omega_z$.

* **Angular Acceleration**: The rate of change of $\omega_z$ defines the $z$-component of angular acceleration:
  $$\alpha_z = \frac{d\omega_z}{dt} = \frac{d^2\theta}{dt^2}$$

* **Kinematic Integrals**: Knowing $\alpha_z(t)$ allows determination of $\omega_z(t)$ via integration, which in turn integrates to yield angular displacement $\theta(t)$:
  $$\omega_z(t) = \omega_z(0) + \int_{0}^{t} \alpha_z(t') \, dt', \quad \theta(t) = \theta(0) + \int_{0}^{t} \omega_z(t') \, dt'$$

* **Rotational Kinetic Energy**: The total rotational kinetic energy of a body rotating about a fixed axis $S$ is expressed as:
  $$K_{\text{rot}} = \frac{1}{2} I_S \omega_z^2$$
  where $I_S$ is the moment of inertia about that axis. Although $\omega_z$ can be negative, its square $\omega_z^2$ is always positive definite.

* **Rotational Power**: The rate at which torque $\tau_{S, z}$ does work on a rotating body is directly proportional to its angular velocity:
  $$P_{\text{rot}} = \tau_{S, z} \omega_z$$

---

## 2. Torque ($\vec{\tau}$)

### 2.1 Vector Definition and Cross Product

Torque measures the twisting or rotational effect of an applied force about a specific pivot point $S$ [110, 120]. For a force $\vec{F}_P$ applied at point $P$, with position vector $\vec{r}_{S,P}$ drawn from pivot $S$ to $P$, torque is defined as the vector cross product:
$$\vec{\tau}_S = \vec{r}_{S,P} \times \vec{F}_P$$

* **Magnitude**:
  $$\tau_S = |\vec{r}_{S,P}| |\vec{F}_P| \sin\theta = r F \sin\theta$$
  where $\theta$ is the angle between $\vec{r}_{S,P}$ and $\vec{F}_P$ ($0 \le \theta \le \pi$).
* **Equivalent Interpretations**:
  1. **Moment Arm ($r_\perp$)**: $\tau_S = r_\perp F$, where $r_\perp = r \sin\theta$ is the perpendicular distance from the pivot $S$ to the line of action of the force.
  2. **Perpendicular Force ($F_\perp$)**: $\tau_S = r F_\perp$, where $F_\perp = F \sin\theta$ is the component of force perpendicular to the position vector $\vec{r}_{S,P}$.

### 2.2 Sign Conventions & Direction (Right-Hand Rule)

* The vector direction of $\vec{\tau}_S$ is perpendicular to the plane formed by $\vec{r}_{S,P}$ and $\vec{F}_P$, given by the **Right-Hand Rule**.
* For 2D coplanar motion about the $z$-axis:
  * **Counterclockwise (CCW)** torque points in the $+\hat{k}$ direction ($\tau_z > 0$).
  * **Clockwise (CW)** torque points in the $-\hat{k}$ direction ($\tau_z < 0$).

### 2.3 Internal Torque Cancellation

For a system of particles or continuous rigid body, internal forces occur in equal and opposite pairs according to Newton's Third Law ($\vec{F}_{j,i} = -\vec{F}_{i,j}$) [31, 143]. Because internal forces act along the straight line connecting the mass elements, their relative position vector $\vec{r}_{S,i} - \vec{r}_{S,j}$ is collinear with $\vec{F}_{j,i}$. Consequently:
$$(\vec{r}_{S,i} - \vec{r}_{S,j}) \times \vec{F}_{j,i} = \vec{0}$$
**Internal torques cancel out in pairs**, meaning net rotational motion is governed solely by **external torques**:
$$\vec{\tau}_S^{\text{net}} = \vec{\tau}_S^{\text{ext}}$$

---

## 3. Moment of Inertia ($I$)

### 3.1 Definition and Physical Meaning

Moment of Inertia $I_S$ is the rotational analog to mass [15, 18]. It quantifies an object's resistance to angular acceleration about a specified rotation axis passing through point $S$:

* **Discrete Mass System**:
  $$I_S = \sum_{j=1}^N \Delta m_j r_{\perp, j}^2$$
* **Continuous Body**:
  $$I_S = \int_{\text{body}} r_\perp^2 \, dm$$
  where $r_\perp$ is the perpendicular distance from the mass element $dm$ to the axis of rotation.
* **SI Units**: $\text{kg} \cdot \text{m}^2$.

*Key Insight*: Unlike translational mass (which is constant), $I$ depends not only on total mass, but also on **how that mass is distributed** relative to the rotation axis [18, 19]. Moving mass farther from the axis dramatically increases $I$ due to the $r_\perp^2$ factor.

### 3.2 Moments of Inertia for Common Standard Shapes

1. **Thin Uniform Rod (length $L$, mass $m$)**:
   * About center of mass: $I_{\text{cm}} = \frac{1}{12} m L^2$
   * About one end: $I_{\text{end}} = \frac{1}{3} m L^2$

2. **Thin Uniform Disc or Solid Cylinder (radius $R$, mass $m$)**:
   * About central axis perpendicular to disc: $I_{\text{cm}} = \frac{1}{2} m R^2$

3. **Solid Uniform Sphere (radius $R$, mass $m$)**:
   * About any central axis: $I_{\text{cm}} = \frac{2}{5} m R^2$

### 3.3 Parallel Axis Theorem

The **Parallel Axis Theorem** relates the moment of inertia $I_S$ about any axis passing through point $S$ to the moment of inertia $I_{\text{cm}}$ about a parallel axis passing through the body's center of mass:
$$I_S = I_{\text{cm}} + m d_{S, \text{cm}}^2$$
where:

* $I_{\text{cm}}$ is the moment of inertia about the parallel axis through the center of mass.
* $m$ is the total mass of the object.
* $d_{S, \text{cm}}$ is the perpendicular separation distance between the two parallel axes.

*Note*: $I_{\text{cm}}$ is the **minimum possible** moment of inertia for any family of parallel axes.

---

## 4. The Rotational Equation of Motion

Combining torque and moment of inertia yields the rotational equivalent of Newton's Second Law ($\vec{F} = m\vec{a}$) for fixed-axis rotation:
$$\tau_{S, z}^{\text{ext}} = I_S \alpha_z$$
where:

* $\tau_{S, z}^{\text{ext}}$ is the net external torque component along the $z$-axis of rotation.
* $I_S$ is the moment of inertia about axis $S$.
* $\alpha_z = \frac{d\omega_z}{dt} = \frac{d^2\theta}{dt^2}$ is the $z$-component of angular acceleration.

---

## 5. Rotational Energy, Work, and Power

* **Rotational Kinetic Energy**:
  $$K_{\text{rot}} = \frac{1}{2} I_S \omega_z^2$$
* **Rotational Work**:
  $$W_{\text{rot}} = \int_{\theta_i}^{\theta_f} \tau_{S, z} \, d\theta$$
* **Work-Kinetic Energy Theorem**:
  $$W_{\text{rot}} = \frac{1}{2} I_S \omega_{z, f}^2 - \frac{1}{2} I_S \omega_{z, i}^2 = \Delta K_{\text{rot}}$$
* **Rotational Power**:
  $$P_{\text{rot}} = \frac{dW_{\text{rot}}}{dt} = \tau_{S, z} \omega_z$$
