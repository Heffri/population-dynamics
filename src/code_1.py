# collection of packages used 

import numpy as np
import matplotlib.pyplot as plt
import time as time
from scipy.integrate import solve_ivp

# ----------------------------------------------------------------------------------------------------------------------- # 

# q1.2
t_end = 60
x = np.linspace(0, t_end, 100)
y = 10 * np.exp(-0.1 * x)

plt.figure(figsize=(16, 6))
plt.plot(x, y)
plt.title("Aphid Population Over Time")
plt.xlabel("Time (days)")
plt.ylabel("Aphid Population")
plt.grid()
plt.savefig("aphid_population.png", dpi=300)

# ----------------------------------------------------------------------------------------------------------------------- # 

# q1.4

# define the ODE \frac{dy}{dt} = -\gamma y
def f(y, t):
    gamma = 0.1  # decay rate
    return -gamma * y

# initial condition
y0 = 10  # initial population
# initial time
t0 = 0
# final time
T = 60
# step size
h = 1

def forward_euler(f, y0, t0, T, h):
    # calculate number of steps
    N = int((T - t0) / h)
    
    # init arrays for time and solution for plotting
    t = np.zeros(N)
    y = np.zeros(N)
    
    # initial values
    t[0] = t0
    y[0] = y0
    
    # Forward Euler iteration
    for i in range(N-1):
        y[i+1] = y[i] + h * f(y[i], t[i])
        t[i+1] = t[i] + h
    
    return t, y

forward_euler_solution = forward_euler(f, y0, t0, T, h)

x = np.linspace(0, t_end, 100)
y_analytical = 10 * np.exp(-0.1 * x)

# plot
plt.figure(figsize=(16, 6))
plt.plot(forward_euler_solution[0], forward_euler_solution[1], label='Forward Euler', color='red')
plt.plot(x, y_analytical, label='Analytical Solution', color='blue')
plt.title("Aphid Population Over Time")
plt.xlabel("Time (days)")
plt.ylabel("Aphid Population")
plt.legend()
plt.grid()
plt.savefig("aphid_population_forward_euler.png", dpi=300)

# ----------------------------------------------------------------------------------------------------------------------- # 

# q1.5

# define the ODE \frac{dy}{dt} = -\gamma y
def f(y, t):
    gamma = 0.1  # decay rate
    return -gamma * y

# initial condition
y0 = 10  # initial population
# initial time
t0 = 0
# final time
T = 60
# step larger step size
h = 21

forward_euler_solution = forward_euler(f, y0, t0, T, h)
x = np.linspace(0, t_end, 100)
y_analytical = 10 * np.exp(-0.1 * x)

# plot
plt.figure(figsize=(16, 6))
plt.plot(forward_euler_solution[0], forward_euler_solution[1], label='Forward Euler', color='red')
plt.plot(x, y_analytical, label='Analytical Solution', color='blue')
plt.title("Aphid Population Over Time")
plt.xlabel("Time (days)")
plt.ylabel("Aphid Population")
plt.legend()
plt.grid()
plt.savefig("aphid_population_forward_euler.png", dpi=300)


# ----------------------------------------------------------------------------------------------------------------------- # 

# q1.6

# define the ODE \frac{dy}{dt} = -\gamma y
def f(y, t):
    gamma = 0.1  # decay rate
    return -gamma * y

# initial condition
y0 = 10  # initial population
# initial time
t0 = 0
# final time
T = 60
# step larger step size
h = 19

forward_euler_solution = forward_euler(f, y0, t0, T, h)
x = np.linspace(0, t_end, 100)
y_analytical = 10 * np.exp(-0.1 * x)

# plot
plt.figure(figsize=(16, 6))
plt.plot(forward_euler_solution[0], forward_euler_solution[1], label='Forward Euler', color='red')
plt.plot(x, y_analytical, label='Analytical Solution', color='blue')
plt.title("Aphid Population Over Time")
plt.xlabel("Time (days)")
plt.ylabel("Aphid Population")
plt.legend()
plt.grid()
plt.savefig("aphid_population_forward_euler.png", dpi=300)



# ----------------------------------------------------------------------------------------------------------------------- # 

# q1.7

# define the ODE \frac{dy}{dt} = -\gamma y
def f(y, t):
    gamma = 0.1  # decay rate
    return -gamma * y

# initial condition
y0 = 10  # initial population
# initial time
t0 = 0
# final time
T = 60
# step larger step size
h_reducing = [5, 8, 11, 14, 17, 20]

plt.figure(figsize=(16, 6))

x_analytical = np.linspace(0, T, 200) # Use more points for smooth analytical curve
y_analytical = 10 * np.exp(-0.1 * x_analytical)
plt.plot(
    x_analytical,
    y_analytical,
    label="Analytical Solution",
    color="blue",
    linestyle="--",
    linewidth=2, # Make analytical line slightly thicker
)


for i, h in enumerate(h_reducing):
    # Assuming forward_euler returns (times, y_values)
    forward_euler_solution = forward_euler(f, y0, t0, T, h)

    # Plot Forward Euler results for the current h
    # Using f-string to add h to the label for clarity in the legend
    plt.plot(
        forward_euler_solution[0],
        forward_euler_solution[1],
        label=f"Forward Euler (h={h})",
        marker='o', # Add markers to see the discrete points
        markersize=4,
        linestyle='-',
    )

plt.grid() 
plt.title("Aphid Population Over Time using Forward Euler")
plt.xlabel("Time (days)")
plt.ylabel("Aphid Population")
plt.legend()
plt.show()




# ----------------------------------------------------------------------------------------------------------------------- # 


# q1.9

t0 = 0                  # initial time
T = 10                  # final time
h = 1                 # step size
y0 = 1                  # initial condition y(0) = 1
gamma = 0.1

# analytical
def analytical_solution(t):
    return y0 * np.exp(-gamma * t) # according to Q1

def second_derivative(t):
    return (gamma**2) * analytical_solution(t)

t1 = t0 + h

# analytical at t1
analytical_solution_t1 = y0 * np.exp(-gamma * t1)
# numerical at t1 
# euler step from y0 at t0: y(t0+h) approx y(t0) + h * f(y(t0), t0)
numerical_solution_t1 = y0 + h * (-gamma * y0)
numerical_lte = analytical_solution_t1 - numerical_solution_t1

# basing answer on Q8
# theoretical term evaluated at t0 (t=0)
y_double_prime_t0 = (gamma**2) * y0 * np.exp(-gamma * t0) # exp(-0)=1
theoretical_lte_t0_value = (h**2 / 2) * y_double_prime_t0

# theoretical term evaluated at t1 (t=0+h)
y_double_prime_t1 = (gamma**2) * y0 * np.exp(-gamma * t1)
theoretical_lte_t1_value = (h**2 / 2) * y_double_prime_t1

print(f"Numerical LTE (first step, h={h}): {numerical_lte:.8f}")
print(f"Theoretical LTE (from y''(t=0)): {theoretical_lte_t0_value:.8f}")
print(f"Theoretical LTE (from y''(t=h)): {theoretical_lte_t1_value:.8f}")



# ----------------------------------------------------------------------------------------------------------------------- # 

# q1.10

t0 = 0                  # initial time
T = 10                  # final time
h = 0.05                # step size
y0 = 1                # initial condition y(0) = 1
gamma = 0.1

# analytical
def analytical_solution(t):
    return y0 * np.exp(-gamma * t) # according to Q1

def second_derivative(t):
    return (gamma**2) * analytical_solution(t)

t1 = t0 + h

# analytical at t1
analytical_solution_t1 = y0 * np.exp(-gamma * t1)
# numerical at t1 
# euler step from y0 at t0: y(t0+h) approx y(t0) + h * f(y(t0), t0)
numerical_solution_t1 = y0 + h * (-gamma * y0)
numerical_lte = analytical_solution_t1 - numerical_solution_t1

# basing answer on Q8
# theoretical term evaluated at t0 (t=0)
y_double_prime_t0 = (gamma**2) * y0 * np.exp(-gamma * t0) # exp(-0)=1
theoretical_lte_t0_value = (h**2 / 2) * y_double_prime_t0

# theoretical term evaluated at t1 (t=0+h)
y_double_prime_t1 = (gamma**2) * y0 * np.exp(-gamma * t1)
theoretical_lte_t1_value = (h**2 / 2) * y_double_prime_t1

print(f"Numerical LTE (first step, h={h}): {numerical_lte:.8f}")
print(f"Theoretical LTE (from y''(t=0)): {theoretical_lte_t0_value:.8f}")
print(f"Theoretical LTE (from y''(t=h)): {theoretical_lte_t1_value:.8f}")



# ----------------------------------------------------------------------------------------------------------------------- # 

# q1.11

# initial condition
y0 = 10  # initial population
# initial time
t0 = 0
# final time
T = 60
# step size
h = 0.0001
start_time = time.time()
slow_forward_euler_solution = forward_euler(f, y0, t0, T, h)
end_time = time.time()
print("Time taken for slow simulation:", end_time - start_time)


# ----------------------------------------------------------------------------------------------------------------------- # 

# q2.2

# according to discretization
def lotka_volterra_step_forward(xt,yt,h, alpha,beta,delta,gamma):
    xnext = xt + h * (alpha*xt - beta*xt*yt)
    ynext = yt + h * (delta*xt*yt - gamma*yt)
    return xnext, ynext

# euler forward method from previous lab 
def forward_euler(x0, y0, t0, T, h, alpha, beta, delta, gamma):
    N = int((T - t0) / h) # number of steps
    xsol = [x0] # array of x values with initial
    ysol = [y0] # ^
    tvalues = [t0]
    for i in range(0, N):
        xnext, ynext = lotka_volterra_step_forward(xsol[i], ysol[i],h, alpha, beta, delta, gamma )
        
        xsol.append(xnext)
        ysol.append(ynext)
        
        tvalues.append(h * i)
        
    return xsol, ysol, tvalues
    
x0 = 10
y0 = 10 
t0 = 0
T = 120
h = 0.0001
alpha = 1.5
beta = 0.3
delta = 0.1
gamma = 0.4

xsol, ysol, tvalues = forward_euler(x0, y0, t0, T, h, alpha, beta, delta, gamma)
plt.figure(figsize=(16, 6))
plt.plot(tvalues, xsol, label="Foxes")
plt.plot(tvalues, ysol, label="Rabbits")
plt.xlabel("Time (in days)")
plt.ylabel("Population")
plt.legend()
plt.grid()



# ----------------------------------------------------------------------------------------------------------------------- # 

# q2.3

x0 = 10
y0 = 10 
t0 = 0
T = 60
h = 0.0001
alpha = 0.3
beta = 0.1
delta = 0.05
gamma = 0.1

xsol, ysol, tvalues = forward_euler(x0, y0, t0, T, h, alpha, beta, delta, gamma)
plt.figure(figsize=(16, 6))
plt.plot(tvalues, xsol, label="Aphids")
plt.plot(tvalues, ysol, label="Tomatoes")
plt.xlabel("Time (in days)")
plt.ylabel("Population")
plt.legend()
plt.grid()



# ----------------------------------------------------------------------------------------------------------------------- # 

# q2.4

alpha = 0.3  
beta = 0.1   
delta = 0.05 
gamma = 0.1  

x0 = 10.0  # Initial number of tomato leaves
y0 = 10.0  # Initial number of aphids

t0 = 0.0   
T = 60.0   

# Step size for the Forward Euler solver
h = 0.001

# We get the time points (tvalues) and corresponding x values (xsol)
xsol_euler, ysol_euler, tvalues_euler = forward_euler(x0, y0, t0, T, h, alpha, beta, delta, gamma)


delta_t = h 

# Calculate the sum (sum of left and right endpoints for each interval)
sum_trapezoids = np.sum(xsol_euler[:-1] + xsol_euler[1:])

# Multiply by (delta_t / 2)
S = (delta_t / 2.0) * sum_trapezoids

# --- Print the result ---
print(f"The success of the tomato plants (S), computed using the trapezoidal rule")
print(f"on the Forward Euler solution (h_euler={h}) over t=[{t0}, {T}] is:")
print(f"S = {S:.4f}")



# ----------------------------------------------------------------------------------------------------------------------- # 


# q2.5

alpha = 0.3  
beta = 0.1   
delta = 0.05 
gamma = 0.1  

x0 = 10.0  # Initial number of tomato leaves
y0 = 11.0  # Initial number of aphids

t0 = 0.0   
T = 60.0   

# Step size for the Forward Euler solver
h = 0.001

# We get the time points (tvalues) and corresponding x values (xsol)
xsol_euler, ysol_euler, tvalues_euler = forward_euler(x0, y0, t0, T, h, alpha, beta, delta, gamma)


delta_t = h 

# Calculate the sum (sum of left and right endpoints for each interval)
sum_trapezoids = np.sum(xsol_euler[:-1] + xsol_euler[1:])

# Multiply by (delta_t / 2)
S = (delta_t / 2.0) * sum_trapezoids

# --- Print the result ---
print(f"The success of the tomato plants (S), computed using the trapezoidal rule with more aphids in the start")
print(f"on the Forward Euler solution (h_euler={h}) over t=[{t0}, {T}] is:")
print(f"S = {S:.4f}")




# ----------------------------------------------------------------------------------------------------------------------- # 





# q2.6

alpha = 0.3  
beta = 0.1   
delta = 0.05 
gamma = 0.09  

x0 = 10.0  # Initial number of tomato leaves
y0 = 10.0  # Initial number of aphids

t0 = 0.0   
T = 60.0   

h = 0.001

# We get the time points (tvalues) and corresponding x values (xsol)
xsol_euler, ysol_euler, tvalues_euler = forward_euler(x0, y0, t0, T, h, alpha, beta, delta, gamma)
delta_t = h 

# Calculate the sum (sum of left and right endpoints for each interval)
sum_trapezoids = np.sum(xsol_euler[:-1] + xsol_euler[1:])

# Multiply by (delta_t / 2)
S = (delta_t / 2.0) * sum_trapezoids

print(f"The success of the tomato plants (S), computed using the trapezoidal rule with super aphids")
print(f"on the Forward Euler solution, (h_euler={h}) over t=[{t0}, {T}] is: S = {S:.4f}")


# ----------------------------------------------------------------------------------------------------------------------- # 

# q2.7

alpha = 0.3  
beta = 0.1   
delta = 0.05 
gamma = 0.1  

x0 = 10.0  # Initial number of tomato leaves
y0 = 10.0  # Initial number of aphids

t0 = 0.0   
T = 60.0   

h = 0.001

# We get the time points (tvalues) and corresponding x values (xsol)
xsol_euler, ysol_euler, tvalues_euler = forward_euler(x0, y0, t0, T, h, alpha, beta, delta, gamma)


delta_t = h 

# Calculate the sum (sum of left and right endpoints for each interval)
sum_trapezoids = np.sum(xsol_euler[:-1] + xsol_euler[1:])

# Multiply by (delta_t / 2)
S = (delta_t / 2.0) * sum_trapezoids

# --- Print the result ---
print(f"The success of the tomato plants (S), computed using the trapezoidal rule if watering more")
print(f"on the Forward Euler solution (h_euler={h}) over t=[{t0}, {T}] is:")
print(f"S = {S:.4f}")




# ----------------------------------------------------------------------------------------------------------------------- # 

# q2.8

from scipy.integrate import solve_ivp
import numpy as np

alpha = 0.3  
beta = 0.1   
delta = 0.05 
gamma = 0.1  

y0_ivp = [10.0, 10.0]
t_span = (0.0, 60.0)

def lotka_volterra(t, y, alpha, beta, delta, gamma):
    """
    Parameters:
    t (float): Current time point (not used in the equations but required by solve_ivp)
    y (array): State vector [x, y] where:
               x = prey population
               y = predator population
    alpha, beta, delta, gamma: Model parameters
    """
    # Unpack the state vector
    x, y = y  
    
    # Prey population rate of change: growth - predation
    dxdt = alpha * x - beta * x * y
    
    # Predator population rate of change: reproduction from predation - natural death
    dydt = delta * x * y - gamma * y
    
    return [dxdt, dydt]  # Return derivatives as a list for solve_ivp

solution_rk45 = solve_ivp(
    lotka_volterra,
    t_span,
    y0_ivp,
    args=(alpha, beta, delta, gamma),
    method='RK45'
)

t_rk45 = solution_rk45.t # Time points selected by RK45
y_rk45 = solution_rk45.y # Solution array [ [x at t1, x at t2, ...], [y at t1, y at t2, ...] ]

# Number of discretization points for RK45
num_points_rk45 = len(t_rk45)

h_euler_decent = 0.001
t0_euler = t_span[0]
T_euler = t_span[1]
num_steps_euler = int(round((T_euler - t0_euler) / h_euler_decent))
num_points_euler = num_steps_euler + 1


print("\n--- Comparison ---")
print(f"RK45 used {num_points_rk45} points.")
print(f"Forward Euler (h={h_euler_decent}) needs {num_points_euler} points.")





# ----------------------------------------------------------------------------------------------------------------------- # 


# q3.1

def lotka_volterra_expanded(x, y, w, alpha, beta, delta, gamma, eta, zeta):
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    dwdt = eta * y * w - zeta * w
    return dxdt, dydt, dwdt



# ----------------------------------------------------------------------------------------------------------------------- # 

# q3.2


alpha = 0.3  # Growth rate of plants
beta = 0.1   # Rate at which aphids consume plants
delta = 0.05  # Growth rate of aphids per plant consumed
gamma = 0.3  # Natural death rate of aphids
eta = 0.1    # growth rate of ladybugs per aphid consumed
zeta = 0.5   # death/migration rate of ladybugs

# Initial conditions: [plants, aphids, ladybugs]
y0_ivp = [10.0, 10.0, 10.0] 

t_span = (0.0, 60.0)


def lotka_volterra_extended(t, y, alpha, beta, delta, gamma, eta, zeta):
    x, y, w = y  #  state vector
    dxdt = alpha * x - beta * x * y  # Plants
    dydt = delta * x * y - gamma * y - eta * y * w  # Aphids
    dwdt = eta * y * w - zeta * w  # Ladybugs
    return [dxdt, dydt, dwdt]

solution_with_ladybugs = solve_ivp(
    lotka_volterra_extended,
    t_span, # ie. 0-60 days
    y0_ivp, # including ladybugs = 10 here
    args=(alpha, beta, delta, gamma, eta, zeta),
    method='RK45',
    dense_output=True # gives continous solution, default is false
)

t_dense = np.linspace(t_span[0], t_span[1], 1000)   
y_dense = solution_with_ladybugs.sol(t_dense) # .sol here provides a continous interpolated solution function, comes from using dense_output = True

S_with_ladybugs = np.trapz(y_dense[0], t_dense) # using inbuilt trapezoidal rule 

# Extract time points and solution
t_with_ladybugs = solution_with_ladybugs.t
y_with_ladybugs = solution_with_ladybugs.y

plt.figure(figsize=(16, 6))
plt.plot(t_with_ladybugs, y_with_ladybugs[0], label='Plants (x)', color='teal')
plt.plot(t_with_ladybugs, y_with_ladybugs[1], label='Aphids (y)', color='orange')
plt.plot(t_with_ladybugs, y_with_ladybugs[2], label='Ladybugs (w)', color='brown')
plt.xlabel('Time (in days)')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model with Plants, Aphids, and Ladybugs')
plt.legend()
plt.grid()
plt.show()




# ----------------------------------------------------------------------------------------------------------------------- # 

# q3.3

from scipy.integrate import solve_ivp
import numpy as np

alpha = 0.3  
beta = 0.1   
delta = 0.05 
gamma = 0.1  

y0_ivp = [10.0, 10.0]
t_span = (0.0, 60.0)

solution_no_ladybugs = solve_ivp(
    lotka_volterra,
    t_span,
    y0_ivp,
    args=(alpha, beta, delta, gamma),
    method='RK45',
    dense_output=True # needed in order to use trapz below, ie. compute integral  
)

y_no_ladybugs_dense = solution_no_ladybugs.sol(t_dense)
S_without_ladybugs = np.trapz(y_no_ladybugs_dense[0], t_dense)

print(f"S with ladybugs: {S_with_ladybugs:.4f}")
print(f"S without ladybugs: {S_without_ladybugs:.4f}")
print(f"Improvement: {S_with_ladybugs - S_without_ladybugs:.4f}")

