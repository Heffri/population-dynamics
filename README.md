# Population Dynamics — Lotka-Volterra Simulation

A Python simulation of predator-prey population dynamics using the Lotka-Volterra equations. Models the cyclical relationship between two competing species over time.

**Course:** Numerical Analysis I — Stockholm University (MM5016)

---

## Background

The Lotka-Volterra system is a pair of nonlinear differential equations describing how predator and prey populations evolve:

$$\frac{dx}{dt} = \alpha x - \beta x y$$

$$\frac{dy}{dt} = \delta x y - \gamma y$$

where $x$ is the prey population, $y$ the predator population, and $\alpha, \beta, \gamma, \delta$ are biological parameters.

## Project Structure

```
population-dynamics/
├── src/
│   └── simulation.py       # Core ODE solver and simulation logic
├── notebooks/
│   └── main.ipynb          # Interactive exploration and visualisation
├── results/
│   └── plots/              # Generated phase portraits and time series
├── data/                   # Parameter sets and initial conditions
├── requirements.txt
└── README.md
```

## Getting Started

```bash
pip install -r requirements.txt
jupyter notebook notebooks/main.ipynb
```

## Results

The simulation produces:
- Time series plots of predator and prey populations
- Phase portraits showing the cyclic attractor in state space

## What's Next

- [ ] Add spatial component (reaction-diffusion / PDE extension)
- [ ] Interactive parameter sweep with sliders (Streamlit or Panel)
- [ ] Stochastic version with demographic noise
- [ ] Fit parameters to real ecological data

## References

- Lotka, A. J. (1925). *Elements of Physical Biology*. Williams & Wilkins.
- Volterra, V. (1926). Variazioni e fluttuazioni del numero d'individui in specie animali conviventi.
