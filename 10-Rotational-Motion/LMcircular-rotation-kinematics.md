# Circular Rotation Kinematics Reference Sheet

This reference sheet summarizes the pure kinematic formulas for circular and planar rotational motion, covering position, velocity, acceleration, unit vector derivatives, constant angular acceleration equations, and non-circular planar extensions.

---

## 1. Polar Coordinates & Unit Vector Derivatives

In planar circular motion of radius $r$, position is described using polar coordinates $(r, \theta(t))$:
$$\vec{r}(t) = r \, \hat{r}(t)$$

### 1.1 Unit Vectors in Cartesian Basis

The radial ($\hat{r}$) and tangential ($\hat{\theta}$) unit vectors are:
$$\hat{r}(t) = \cos\theta(t)\,\hat{i} + \sin\theta(t)\,\hat{j}$$
$$\hat{\theta}(t) = -\sin\theta(t)\,\hat{i} + \cos\theta(t)\,\hat{j}$$

### 1.2 Time Derivatives of Unit Vectors

Applying the chain rule yields the fundamental time derivatives of the moving unit vectors:
$$\frac{d\hat{r}}{dt} = \frac{d\theta}{dt} \, \hat{\theta}(t) = \omega_z \, \hat{\theta}(t)$$
$$\frac{d\hat{\theta}}{dt} = -\frac{d\theta}{dt} \, \hat{r}(t) = -\omega_z \, \hat{r}(t)$$

---

## 2. Angular Kinematic Variables & Vector Relations

### 2.1 Angular Velocity ($\vec{\omega}$)

For fixed-axis rotation along the $z$-axis:
$$\omega_z \equiv \frac{d\theta}{dt}$$
$$\vec{\omega} = \frac{d\theta}{dt} \, \hat{k} = \omega_z \, \hat{k}$$

* **SI Units**: $\text{rad} \cdot \text{s}^{-1}$.
* **Right-Hand Rule**: $\omega_z > 0$ for counterclockwise rotation ($+\hat{k}$), and $\omega_z < 0$ for clockwise rotation ($-\hat{k}$).

### 2.2 Linear & Tangential Velocity ($\vec{v}$)

$$\vec{v}(t) = \frac{d\vec{r}}{dt} = r \frac{d\theta}{dt} \, \hat{\theta}(t) = v_\theta \, \hat{\theta}(t)$$
$$v_\theta = r \omega_z$$
Vector cross product relation:
$$\vec{v} = \vec{\omega} \times \vec{r} = \left(\frac{d\theta}{dt} \hat{k}\right) \times (r \hat{r}) = r \frac{d\theta}{dt} \, \hat{\theta}$$

### 2.3 Angular Acceleration ($\vec{\alpha}$)

$$\alpha_z \equiv \frac{d\omega_z}{dt} = \frac{d^2\theta}{dt^2}$$
$$\vec{\alpha} = \frac{d^2\theta}{dt^2} \, \hat{k} = \alpha_z \, \hat{k}$$

* **SI Units**: $\text{rad} \cdot \text{s}^{-2}$.

---

## 3. Tangential and Radial (Centripetal) Acceleration

Differentiating the velocity vector $\vec{v}(t) = r \omega_z \hat{\theta}(t)$ with respect to time yields two orthogonal acceleration components:
$$\vec{a}(t) = a_r \hat{r}(t) + a_\theta \hat{\theta}(t)$$

### 3.1 Tangential Acceleration ($a_\theta$)

Changes the **magnitude** of the velocity (speed):
$$a_\theta = r \frac{d^2\theta}{dt^2} = r \alpha_z$$

### 3.2 Radial / Centripetal Acceleration ($a_r$)

Changes the **direction** of the velocity vector and points radially inward toward the center of rotation:
$$a_r = -r \left(\frac{d\theta}{dt}\right)^2 = -r \omega_z^2 = -\frac{v_\theta^2}{r}$$
In vector form:
$$\vec{a}_r = -r \omega_z^2 \, \hat{r}(t)$$

---

## 4. Uniform Circular Motion Kinematics

When tangential acceleration is zero ($a_\theta = 0$), speed $v = r|\omega_z|$ is constant.

### 4.1 Period ($T$) and Frequency ($f$)

* **Period ($T$)**: Time to complete one revolution ($s = 2\pi r = v T$):
  $$T = \frac{2\pi r}{v} = \frac{2\pi}{\omega}$$
* **Frequency ($f$)**: Number of revolutions per unit time ($f = 1/T$):
  $$f = \frac{1}{T} = \frac{\omega}{2\pi}$$
  * **SI Unit**: Hertz ($\text{Hz} = \text{s}^{-1}$) [128].

### 4.2 Alternative Centripetal Acceleration Formulas

$$|a_r| = r \omega^2 = \frac{v^2}{r} = 4\pi^2 r f^2 = \frac{4\pi^2 r}{T^2}$$

---

## 5. Kinematic Equations for Constant Angular Acceleration

When angular acceleration is constant ($\alpha_z = \text{const}$), integration yields kinematic equations directly analogous to 1D linear motion:

1. **Angular Velocity Equation**:
   $$\omega_z(t) = \omega_{z,0} + \alpha_z t$$
2. **Angular Position Equation**:
   $$\theta(t) = \theta_0 + \omega_{z,0} t + \frac{1}{2} \alpha_z t^2$$
3. **Rotational Timeless Equation**:
   $$\omega_z^2 = \omega_{z,0}^2 + 2 \alpha_z (\theta - \theta_0)$$
4. **Average Velocity Displacement**:
   $$\theta(t) - \theta_0 = \left(\frac{\omega_{z,0} + \omega_z}{2}\right) t$$

### 5.1 General Kinematic Integrals (Non-Constant $\alpha_z$)

For time-varying $\alpha_z(t)$:
$$\omega_z(t) = \omega_{z,0} + \int_{0}^{t} \alpha_z(t') \, dt'$$
$$\theta(t) = \theta_0 + \int_{0}^{t} \omega_z(t') \, dt'$$

---

## 6. Non-Circular Planar Kinematics (General Extension)

For non-circular trajectories in a plane (e.g., spirals where $r = r(t)$) [144, 145]:
$$\vec{r}(t) = r(t) \, \hat{r}(t)$$

### 6.1 Velocity Vector

$$\vec{v}(t) = \frac{dr}{dt} \hat{r} + r \frac{d\theta}{dt} \hat{\theta} = v_r \hat{r} + v_\theta \hat{\theta}$$

### 6.2 Acceleration Vector

$$\vec{a}(t) = a_r \hat{r} + a_\theta \hat{\theta}$$

* **Radial Acceleration**:
  $$a_r = \frac{d^2r}{dt^2} - r \left(\frac{d\theta}{dt}\right)^2$$
* **Tangential Acceleration**:
  $$a_\theta = r \frac{d^2\theta}{dt^2} + 2 \frac{dr}{dt} \frac{d\theta}{dt}$$
* **Coriolis Acceleration Term**:
  $$a_{\text{cor}} = 2 \frac{dr}{dt} \frac{d\theta}{dt}$$
