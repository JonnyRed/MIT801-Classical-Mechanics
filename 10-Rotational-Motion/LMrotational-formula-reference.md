# Rotational Motion Formula Reference

Formulas from the circular-rotation kinematics and rotational-dynamics notes, grouped by topic. Here, $\omega_z$ is the signed angular-velocity component, while $\omega = |\omega_z|$ is angular speed.

## 1. Polar Coordinates and Unit Vectors

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Position, circular path | $\vec{r}(t) = r\,\hat{r}(t)$ | Radius $r$ is constant. | m |
| Radial unit vector | $\hat{r}(t) = \cos\theta(t)\,\hat{i} + \sin\theta(t)\,\hat{j}$ | In the plane of motion. | Dimensionless |
| Tangential unit vector | $\hat{\theta}(t) = -\sin\theta(t)\,\hat{i} + \cos\theta(t)\,\hat{j}$ | Perpendicular to $\hat{r}$ in the direction of increasing $\theta$. | Dimensionless |
| Radial unit-vector derivative | $\frac{d\hat{r}}{dt} = \omega_z\,\hat{\theta}$ | $\omega_z = d\theta/dt$. | s$^{-1}$ |
| Tangential unit-vector derivative | $\frac{d\hat{\theta}}{dt} = -\omega_z\,\hat{r}$ | $\omega_z = d\theta/dt$. | s$^{-1}$ |

## 2. Angular Kinematics

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Angular velocity component | $\omega_z = \frac{d\theta}{dt}$ | Signed rate of change of angular position. | rad/s |
| Angular velocity vector | $\vec{\omega} = \omega_z\,\hat{k}$ | Fixed-axis rotation about $z$. | rad/s |
| Angular acceleration component | $\alpha_z = \frac{d\omega_z}{dt} = \frac{d^2\theta}{dt^2}$ | Signed rate of change of angular velocity. | rad/s$^2$ |
| Angular acceleration vector | $\vec{\alpha} = \alpha_z\,\hat{k}$ | Fixed-axis rotation about $z$. | rad/s$^2$ |
| Speeding up | $\omega_z\alpha_z > 0$ | Angular velocity and acceleration have the same sign. | Sign criterion; no standalone unit |
| Slowing down | $\omega_z\alpha_z < 0$ | Angular velocity and acceleration have opposite signs. | Sign criterion; no standalone unit |
| Angular velocity from acceleration | $\omega_z(t) = \omega_{z,0} + \int_0^t \alpha_z(t')\,dt'$ | General time-dependent angular acceleration. | rad/s |
| Angular position from velocity | $\theta(t) = \theta_0 + \int_0^t \omega_z(t')\,dt'$ | General angular velocity. | rad |

## 3. Circular-Path Velocity and Acceleration

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Velocity vector | $\vec{v} = \frac{d\vec{r}}{dt} = r\omega_z\,\hat{\theta}$ | Circular path with constant radius. | m/s |
| Tangential velocity | $v_\theta = r\omega_z$ | Signed component along $\hat{\theta}$. | m/s |
| Angular-to-linear velocity | $\vec{v} = \vec{\omega}\times\vec{r}$ | Fixed-axis rotation. | m/s |
| Acceleration decomposition | $\vec{a} = a_r\,\hat{r} + a_\theta\,\hat{\theta}$ | Circular path with constant radius. | m/s$^2$ |
| Tangential acceleration | $a_\theta = r\alpha_z$ | Changes the speed. | m/s$^2$ |
| Radial acceleration component | $a_r = -r\omega_z^2 = -\frac{v_\theta^2}{r}$ | Negative sign indicates inward direction relative to $\hat{r}$. | m/s$^2$ |
| Radial acceleration vector | $\vec{a}_r = -r\omega_z^2\,\hat{r}$ | Points toward the center. | m/s$^2$ |
| Centripetal acceleration magnitude | $\lvert a_r\rvert = r\omega^2 = \frac{v^2}{r} = 4\pi^2rf^2 = \frac{4\pi^2r}{T^2}$ | Uniform circular motion; $v$ and $\omega$ are speeds. | m/s$^2$ |

## 4. Uniform Circular Motion

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Speed | $v = r\omega$ | $\omega = \lvert\omega_z\rvert$. | m/s |
| Period | $T = \frac{2\pi r}{v} = \frac{2\pi}{\omega}$ | Time for one revolution. | s |
| Frequency | $f = \frac{1}{T} = \frac{\omega}{2\pi}$ | Revolutions per unit time; $\omega = \lvert\omega_z\rvert$. | Hz (s$^{-1}$) |
| Period-frequency relation | $fT = 1$ | Uniform periodic motion. | Dimensionless |

## 5. Constant Angular Acceleration

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Angular velocity | $\omega_z(t) = \omega_{z,0} + \alpha_z t$ | Constant $\alpha_z$. | rad/s |
| Angular position | $\theta(t) = \theta_0 + \omega_{z,0}t + \frac{1}{2}\alpha_z t^2$ | Constant $\alpha_z$. | rad |
| Timeless angular equation | $\omega_z^2 = \omega_{z,0}^2 + 2\alpha_z(\theta - \theta_0)$ | Constant $\alpha_z$. | rad$^2$/s$^2$ |
| Average-angular-velocity relation | $\theta(t)-\theta_0 = \left(\frac{\omega_{z,0}+\omega_z}{2}\right)t$ | Constant $\alpha_z$. | rad |

## 6. Variable-Radius Planar Motion

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Position | $\vec{r}(t) = r(t)\,\hat{r}(t)$ | Planar path with changing radius. | m |
| Velocity decomposition | $\vec{v} = \dot{r}\,\hat{r} + r\dot{\theta}\,\hat{\theta}$ | $v_r = \dot{r}$ and $v_\theta = r\dot{\theta}$. | m/s |
| Radial acceleration | $a_r = \ddot{r} - r\dot{\theta}^{2}$ | Component along $\hat{r}$. | m/s$^2$ |
| Tangential acceleration | $a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta}$ | Component along $\hat{\theta}$. | m/s$^2$ |
| Coriolis term | $a_{\text{cor}} = 2\dot{r}\dot{\theta}$ | Part of tangential acceleration when radius changes. | m/s$^2$ |

## 7. Torque and Rotational Dynamics

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Torque vector | $\vec{\tau}_S = \vec{r}_{S,P}\times\vec{F}_P$ | Moment of force about pivot $S$. | N m |
| Torque magnitude | $\tau_S = rF\sin\phi$ | $\phi$ is the angle between $\vec{r}_{S,P}$ and $\vec{F}_P$. | N m |
| Moment-arm form | $\tau_S = r_\perp F$ | $r_\perp = r\sin\phi$ is the perpendicular lever arm. | N m |
| Perpendicular-force form | $\tau_S = rF_\perp$ | $F_\perp = F\sin\phi$. | N m |
| Internal torque pair | $(\vec{r}_{S,i}-\vec{r}_{S,j})\times\vec{F}_{j,i}=\vec{0}$ | For equal-and-opposite internal forces along the line joining particles. | N m |
| Net torque | $\vec{\tau}_S^{\text{net}} = \vec{\tau}_S^{\text{ext}}$ | Internal torques cancel for the stated particle-system assumptions. | N m |
| Rotational equation of motion | $\tau_{S,z}^{\text{ext}} = I_S\alpha_z$ | Fixed-axis rotation about $z$. | N m |

## 8. Moment of Inertia

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Discrete system | $I_S = \sum_{j=1}^{N}\Delta m_j r_{\perp,j}^{2}$ | $r_{\perp,j}$ is each mass element's distance from the axis. | kg m$^2$ |
| Continuous body | $I_S = \int_{\text{body}} r_\perp^2\,dm$ | Integrate squared perpendicular distance over the mass distribution. | kg m$^2$ |
| Thin rod, center axis | $I_{\text{cm}} = \frac{1}{12}mL^2$ | Uniform rod, axis through center and perpendicular to rod. | kg m$^2$ |
| Thin rod, end axis | $I_{\text{end}} = \frac{1}{3}mL^2$ | Uniform rod, axis through one end and perpendicular to rod. | kg m$^2$ |
| Solid disc or cylinder | $I_{\text{cm}} = \frac{1}{2}mR^2$ | Uniform body, central symmetry axis. | kg m$^2$ |
| Solid sphere | $I_{\text{cm}} = \frac{2}{5}mR^2$ | Uniform sphere, any axis through its center. | kg m$^2$ |
| Parallel-axis theorem | $I_S = I_{\text{cm}} + md_{S,\text{cm}}^2$ | Parallel axes separated by perpendicular distance $d_{S,\text{cm}}$. | kg m$^2$ |

## 9. Rotational Energy, Work, and Power

| Quantity | Formula | Meaning or condition | SI units |
| --- | --- | --- | --- |
| Rotational kinetic energy | $K_{\text{rot}} = \frac{1}{2}I_S\omega_z^2$ | Fixed-axis rotation; nonnegative and independent of rotation direction. | J |
| Rotational work | $W_{\text{rot}} = \int_{\theta_i}^{\theta_f}\tau_{S,z}\,d\theta$ | Work by torque over angular displacement. | J |
| Work-energy theorem | $W_{\text{rot}} = \frac{1}{2}I_S\omega_{z,f}^2 - \frac{1}{2}I_S\omega_{z,i}^2 = \Delta K_{\text{rot}}$ | Constant $I_S$ about the rotation axis. | J |
| Rotational power | $P_{\text{rot}} = \frac{dW_{\text{rot}}}{dt} = \tau_{S,z}\omega_z$ | Instantaneous power for fixed-axis rotation. | W |
