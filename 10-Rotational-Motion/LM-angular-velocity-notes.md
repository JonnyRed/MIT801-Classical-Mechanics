# Angular Velocity and $\omega_z = \frac{d\theta}{dt}$

The formula **$\omega_z = \frac{d\theta}{dt}$** defines the **$z$-component of the angular velocity vector** for a rigid body undergoing fixed-axis rotation. In the broader framework of rotational kinematics and dynamics, this relation serves as the fundamental link between an object's changing angular position, its vector representation of rotation, its linear velocity at individual points, and its overall rotational energy.

---

1. Component vs. Vector Representation

* **The Scalar Component ($\omega_z$)**: The quantity $\omega_z \equiv \frac{d\theta}{dt}$ is the time derivative of the angle $\theta$ that describes the rotational position of a reference line in the plane of rotation. It measures the rate at which this angle changes over time.
* **The Angular Velocity Vector ($\vec{\omega}$)**: Angular velocity is fundamentally a vector quantity. For rotation about a fixed $z$-axis, the angular velocity vector is directed along the axis of rotation perpendicular to the plane of motion:
  $$\vec{\omega} = \frac{d\theta}{dt} \hat{k} = \omega_z \hat{k}$$
  where $\hat{k}$ is the unit vector along the $z$-axis.

---

2. Sign Convention and Direction (Right-Hand Rule)

Because $\omega_z$ is an algebraic component, it can be positive, zero, or negative:

* **Counterclockwise Rotation**: Using a standard right-handed coordinate system, if the object rotates counterclockwise when viewed from above the plane of rotation, $\theta$ increases with time ($\omega_z > 0$) and $\vec{\omega}$ points in the **$+\hat{k}$ direction**.
* **Clockwise Rotation**: If the object rotates clockwise, $\theta$ decreases with time ($\omega_z < 0$) and $\vec{\omega}$ points in the **$-\hat{k}$ direction**.
* **Right-Hand Rule**: The vector direction is established by curling the fingers of the right hand in the direction of rotation; the extended right thumb points in the direction of $\vec{\omega}$.

---

3. Uniformity Across a Rigid Body

A defining property of a **rigid body** in fixed-axis rotation is that **every single mass element or point in the body shares the exact same angular velocity $\omega_z$** at any instant. If different parts of the object possessed different angular velocities, mass elements would catch up to or pass one another, which would violate the rigid-body condition that inter-point distances remain fixed.

---

4. Broader Context in Kinematics and Dynamics

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
