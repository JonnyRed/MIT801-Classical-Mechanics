# Classical Mechanics Project - MIT 8.01SC

This project follows the MIT OpenCourseWare 8.01SC Classical Mechanics curriculum,
implementing concepts using SymPy and its mechanics package for symbolic
computation and analysis.

## Course Overview

MIT 8.01SC Classical Mechanics introduces the fundamental concepts of
classical mechanics including:

- Vector kinematics and coordinate systems
- Newton's laws of motion
- Force analysis and free body diagrams
- Work, energy, and conservation laws
- Momentum and collisions
- Rotational motion and angular momentum
- Oscillations and waves
- Gravitation
- Special relativity basics

## Environment Setup

### Prerequisites

- Python 3.11+ (recommended)
- Conda environment manager

### Installation

1. **Create conda environment:**

   ```bash
   conda create -n classical-mechanics python=3.11 -y
   conda activate classical-mechanics
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**

   ```python
   import sympy as sp
   from sympy.physics.mechanics import *
   print(f"SymPy version: {sp.__version__}")
   ```

## Project Structure

```text
MIT801-Classical Mechanics/
├── 01-Vector-Kinematics/          # Vector algebra and kinematics
├── 02-Newtons-Laws/              # Newton's laws and force analysis
├── 03-Force-and-Motion/          # Applications of Newton's laws
├── 04-Work-and-Energy/           # Work-energy theorem and conservation
├── 05-Momentum-and-Collisions/   # Linear momentum and collisions
├── 06-Rotational-Motion/         # Rotational dynamics
├── 07-Angular-Momentum/          # Angular momentum conservation
├── 08-Oscillations/              # Simple harmonic motion
├── 09-Gravitation/              # Newton's law of gravitation
├── 10-Special-Relativity/        # Introduction to special relativity
├── examples/                     # Additional example problems
├── solutions/                    # Problem solutions
├── figures/                      # Diagrams and visualizations
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Key Features

### SymPy Mechanics Integration

- Symbolic vector operations and reference frames
- Particle and rigid body dynamics
- Automated equation of motion derivation
- Energy and momentum calculations

### Interactive Jupyter Notebooks

Each topic includes:

- Theoretical foundations with SymPy implementations
- Worked examples and problem-solving techniques
- Numerical simulations and visualizations
- Interactive parameter exploration

### Comprehensive Coverage

- **Vector Kinematics**: Position, velocity, acceleration in multiple coordinate systems
- **Newton's Laws**: Force analysis, free body diagrams, equilibrium
- **Work & Energy**: Work-energy theorem, conservation laws, power
- **Momentum**: Linear and angular momentum, collision analysis
- **Rotational Motion**: Rigid body dynamics, moment of inertia
- **Oscillations**: Simple harmonic motion, damped and driven oscillators
- **Gravitation**: Orbital mechanics, Kepler's laws
- **Special Relativity**: Lorentz transformations, relativistic dynamics

## Usage Examples

### Basic Vector Operations

```python
import sympy as sp
from sympy.physics.mechanics import *

# Define reference frame
N = ReferenceFrame('N')

# Create vectors
r1 = 3*N.x + 4*N.y + 5*N.z
r2 = 2*N.x - N.y + 3*N.z

# Vector operations
result = r1.cross(r2)
print(f"Cross product: {result}")
```

### Particle Dynamics

```python
# Define particle
particle = Particle('particle', mass=sp.symbols('m'))

# Define position as function of time
t = sp.symbols('t')
x = sp.Function('x')(t)
r = x*N.x

# Calculate velocity and acceleration
v = r.diff(t)
a = v.diff(t)

# Apply Newton's second law
F = particle.mass * a
```

### Energy Analysis

```python
# Kinetic and potential energy
m, g, h = sp.symbols('m g h', positive=True)
v = sp.symbols('v', positive=True)

KE = sp.Rational(1, 2) * m * v**2
PE = m * g * h
E_total = KE + PE
```

## Dependencies

### Core Packages

- **SymPy** (≥1.12.0): Symbolic mathematics and mechanics
- **NumPy** (≥1.24.0): Numerical computations
- **Matplotlib** (≥3.7.0): Plotting and visualization
- **SciPy** (≥1.10.0): Scientific computing tools

### Jupyter Environment

- **Jupyter** (≥1.0.0): Interactive notebook environment
- **IPython** (≥6.20.0): Enhanced Python shell
- **Jupyter Book** (≥0.15.0): Documentation generation

## Learning Path

### Beginner Level

1. Start with `01-Vector-Kinematics/01-Vector-Algebra.ipynb`
2. Progress through `02-Newtons-Laws/02-Force-Analysis.ipynb`
3. Explore `04-Work-and-Energy/04-Work-Energy-Theorem.ipynb`

### Intermediate Level

1. Study momentum and collisions in module 05
2. Learn rotational dynamics in modules 06-07
3. Master oscillatory motion in module 08

### Advanced Topics

1. Explore gravitation and orbital mechanics
2. Introduction to special relativity concepts
3. Advanced problem-solving in examples directory

## Problem Solving Approach

Each notebook follows a structured approach:

1. **Theory**: Mathematical foundations with SymPy
2. **Examples**: Worked problems with step-by-step solutions
3. **Analysis**: Symbolic manipulation and simplification
4. **Visualization**: Plots and diagrams for intuition
5. **Numerics**: Parameter studies and specific cases

## Contributing

To add new content:

1. Create notebooks in appropriate topic directories
2. Follow existing naming conventions
3. Include both symbolic and numerical examples
4. Add comprehensive documentation
5. Update README if adding new topics

## Resources

### MIT OCW Course

- [MIT 8.01SC Classical Mechanics](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/)
- Course materials, lectures, and problem sets

### SymPy Documentation

- [SymPy Physics Mechanics](https://docs.sympy.org/latest/modules/physics/mechanics/index.html)
- Vector calculus and reference frames

### Recommended Textbooks

- *Classical Mechanics* by John R. Taylor
- *Introduction to Classical Mechanics* by Daniel Kleppner and Robert Kolenkow
- *Fundamentals of Physics* by Halliday, Resnick, and Walker

## License

This project follows the same license as MIT OpenCourseWare materials
or educational use.

## Acknowledgments

- MIT OpenCourseWare for the 8.01SC curriculum
- SymPy developers for the mechanics package
- Classical mechanics education community

---

**Note**: This project is designed for educational purposes and follows
the MIT 8.01SC curriculum structure. All implementations use symbolic
computation to emphasize fundamental principles over numerical approximations.
