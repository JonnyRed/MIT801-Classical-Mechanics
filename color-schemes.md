# Visualization & Diagramming Conventions

## Classical Mechanics Color Palette

Standardized color-coding system optimized for classical mechanics diagrams. Using distinct colors for different physical quantities prevents confusion when multiple vectors overlap.

| Quantity | Color | Hex | Purpose |
| --- | --- | --- | --- |
| Displacement ($\Delta\vec{r}$) | Violet | #8A2BE2 | Change in position from initial to final point |
| Impulse ($\vec{J}$) | Electric Indigo | #4D00FF | Change in momentum; highlights brief high-force events |
| Net / Resultant Force | Crimson Red | #CC0000 | Vector sum ($\vec{F}_{\text{net}}$); use thick lines |
| Component Forces | Light Red | #FF6666 | Resolved forces ($F_x$, $F_y$); use 50% opacity |
| Applied Forces | Royal Blue | #0066CC | External pushes, pulls, tensions ($\vec{T}$), normal forces ($\vec{N}$) |
| Resistive Forces | Charcoal Grey | #4D4D4D | Friction ($\vec{f}$), air resistance; subtle, passive |
| Velocity | Emerald Green | #00994D | Direction of motion ($\vec{v}$); distinguishes from forces |
| Acceleration | Vibrant Orange | #FF8000 | Acceleration ($\vec{a}$); often drawn offset |
| Momentum | Deep Navy Blue | #002266 | Linear momentum ($\vec{p} = m\vec{v}$); parallel offset from velocity |

## Rotational Mechanics Color Palette

High-contrast extension specifically for rotational mechanics. These colors are designed to stand out clearly when overlaid on linear forces and velocity arrows.

| Quantity | Color | Hex | Purpose |
| --- | --- | --- | --- |
| Torque ($\vec{\tau}$) | Deep Purple | #6600CC | Rotational force; draw as curved arrow around pivot |
| Angular Velocity ($\vec{\omega}$) | Teal / Cyan | #009999 | Rotation rate and direction; complements linear velocity |
| Angular Acceleration ($\vec{\alpha}$) | Coral Orange | #FF6B35 | Change in angular velocity |
| Angular Momentum ($\vec{L}$) | Slate Blue | #6A5ACD | Rotational momentum |
| Moment Arm / Lever Arm | Light Teal | #66CCCC | Distance line for torque calculation; use dashed lines |

## Tips for Effective Diagrams

### Avoiding Visual Confusion

**Velocity vs. Momentum:**
Because momentum and velocity always point in the same direction, they will overlap if drawn directly on top of each other.

Strategy for Draw.io:
1. Draw your Velocity arrow (#00994D Green) originating directly from the center of the object
2. Draw your Momentum arrow (#002266 Navy) slightly higher or lower, running perfectly parallel
3. Use a slightly thinner line weight (1.5pt) for the momentum arrow so it doesn't crowd the velocity vector

**Multiple Forces:**
- Use 50% opacity for component forces so they sit quietly beneath the net force
- Use thick lines (2–2.5pt) for net/resultant forces to make them dominant
- Group related forces (e.g., all drag forces) with similar styling

### Quick Styling Shortcuts in Draw.io

**Shortcut 1: Format Painter (Copy/Paste Styles)**
- Style one arrow perfectly (e.g., Green, 2pt thickness, 50% opacity for velocity)
- Select that arrow and press **Ctrl+Shift+C** (or **Cmd+Shift+C** on Mac) to copy its style
- Select any new arrow and press **Ctrl+Shift+V** (or **Cmd+Shift+V** on Mac) to paste the exact color and transparency instantly

**Shortcut 2: Add Colors to Your Palette**
- Select an arrow and click the Line Color box in the right-hand Format Panel
- Type one of the hex codes above into the color picker box
- Click the **+** icon in the "Remembered" colors section at the bottom to lock it into your workspace for the rest of your session

### Best Practices

| Element | Guideline | Reasoning |
| --- | --- | --- |
| Vectors originating from object | Forces, velocity, acceleration | Shows where the effect is applied |
| Vectors drawn offset | Momentum, angular momentum | Avoids visual overlap with parallel quantities |
| Dashed lines | Moment arms, construction lines, component guides | Distinguishes them from physical quantities |
| Thick lines (2–2.5pt) | Net force, resultant vectors | Makes dominant quantities visually prominent |
| Thin lines (1–1.5pt) | Component forces, momentum | Allows them to recede visually |
| 50% opacity | Component vectors, secondary forces | Prevents cluttering the diagram |
| Solid lines | Primary vectors, applied forces | Standard, most visible |

## Common Diagram Scenarios

### Circular Motion Diagram

- **Position vector**: Blue (#0066CC), solid, 2pt
- **Velocity vector**: Green (#00994D), solid, 2pt (tangent to circle)
- **Acceleration vector**: Orange (#FF8000), solid, 2pt (pointing toward center)
- **Centripetal force**: Red (#CC0000), solid, 2.5pt (pointing toward center)
- **Moment arm** (for torque): Teal dashed (#66CCCC), 1.5pt

### Rotational Dynamics Diagram

- **Angular velocity**: Teal (#009999), curved arrow, 2pt
- **Torque**: Purple (#6600CC), curved arrow around pivot, 2.5pt
- **Angular momentum**: Slate Blue (#6A5ACD), curved or linear depending on context, 2pt
- **Moment arm**: Light Teal dashed (#66CCCC), 1.5pt
- **Applied force**: Blue (#0066CC), solid, 2pt
- **Pivot point**: Black circle, small, clearly marked

---

## References

- https://maker.pro/custom/tutorial/what-is-torque-and-why-does-it-matter
- https://ilg.physics.ucsb.edu/Courses/6/AL/?linkfile=lab4
