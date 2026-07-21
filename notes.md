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

## The Universal Mechanics Color Palette

Here is a standardized, high-contrast color-coding system optimized for classical mechanics diagrams. Using distinct colors for different physical quantities prevents your diagrams from becoming confusing when multiple vectors overlap.

 **Color Coding System**

| Vector Type           | Recommended Color    | Hex Code | Purpose & Best Practices                                                                                    |
|-----------------------|----------------------|----------|-------------------------------------------------------------------------------------------------------------|
| Net / Resultant Force | Crimson Red          | #CC0000  | Shows the final vector sum ($\vec{F}_{net}$). Use a thick line weight to make it dominant.                  |
| Component Forces      | Light / Rose Red     | #FF6666  | Used for resolved forces (like $F_{x}$ and $F_{y}$). Set to 50% opacity to sit quietly under the net force. |
| Applied Forces        | Royal Blue           | #0066CC  | Represents active external pushes, pulls, tensions ($\vec{T}$), or normal forces ($\vec{N}$).               |
| Resistive Forces      | Charcoal / Dark Grey | #4D4D4D  | Represents friction ($\vec{f}$) or air resistance. Keeps passive, opposing forces subtle.                   |
| Velocity              | Emerald Green        | #00994D  | Shows the direction of motion ($\vec{v}$). Easily distinguishes movement from the forces causing it.        |
| Acceleration          | Vibrant Orange       | #FF8000  | Shows acceleration ($\vec{a}$). Often drawn offset or floating next to the object, rather than attached.    |

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

| Vector / Quantity [2, 3, 4, 5, 6]               | Recommended Color  | Hex Code | Purpose & Best Practices                                                                                                                 |
|-------------------------------------------------|--------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------|
| Torque ($\vec{\tau}$)                           | Deep Purple        | #6600CC  | Represents rotational force. Use thick lines, often drawn as a curved arrow wrapping around a pivot point.                               |
| Angular Velocity ($\vec{\omega}$)               | Teal / Cyan        | #009999  | Shows the speed and direction of rotation. Complements the emerald green used for linear velocity.                                       |
| Angular Momentum ($\vec{L}$)                    | Magenta / Pink     | #CC0066  | Represents rotational momentum. Highly visible when drawn along the axis of rotation using the right-hand rule.                          |
| Centripetal / Radial Acceleration ($\vec{a}_c$) | Gold / Deep Yellow | #E6B800  | Points directly inward toward the center of the circular path. Distinct from the vibrant orange used for linear/tangential acceleration. |

----

## 🎨 How to Use These for Rotational Visuals in Draw.io

Because rotational quantities are often represented as 3D concepts on a 2D canvas, use these styling tweaks to make them clear:

- The Right-Hand Rule (Linear Axes): When drawing $\vec{\omega}$ or $\vec{L}$ acting along a straight axis of rotation, make these arrows thicker (3pt) than your standard force lines to show they represent an entire rotational system.
- Curved Trajectories: For the curved arrows showing the direction of spin, use the Teal or Deep Purple with the Curve connector setting. Set the opacity to 70% if the curve passes over a solid body or mass.

----

[1] [https://maker.pro](https://maker.pro/custom/tutorial/what-is-torque-and-why-does-it-matter)

[2] [https://ilg.physics.ucsb.edu](https://ilg.physics.ucsb.edu/Courses/6/AL/?linkfile=lab4)

[3] [https://phys.libretexts.org](https://phys.libretexts.org/Courses/Georgia_State_University/GSU-TM-Physics_I_%282211%29/03%3A__Relative_and_Rotational_Motion/3.02%3A_Rotational_Variables)

[4] [https://www.vaia.com](https://www.vaia.com/en-us/textbooks/physics/21st-century-astronomy-4-edition/chapter-7/problem-30-how-does-the-law-of-conservation-of-angular-momen/)

[5] [https://en.wikipedia.org](https://en.wikipedia.org/wiki/Angular_velocity)

[6] [https://ilg.physics.ucsb.edu](https://ilg.physics.ucsb.edu/Courses/6/AL/?linkfile=lab4)
