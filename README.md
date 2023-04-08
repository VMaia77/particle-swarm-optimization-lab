## **ParticleSwarmOptimizationLab**

The aim of this project was to implement the Particle Swarm Optimization (PSO) algorithm and its variants, allowing easy implementation of new features and customizations.

The current implementation consists of a standard version of the algorithm, without variations or customizations.

Constraints functions are allowed. When constraints functions are used the algorithm will ignore the non feasible solutions in the updates (but positions are always updated). In addition, penalties can be added to the objective function values to deal with constraints.

### **Overview**

Particle Swarm Optimization is a metaheuristic optimization algorithm that is inspired by the behavior of particles moving in a search space (defined by a function). The PSO algorithm involves creating a swarm of particles that move around in a search space to find the optimal solution to a given problem. Therefore, the algorithm is suitable for complex nonlinear functions, non differentiable functions and black-box functions.

Although the algorithm don't uses derivatives/gradients by default, in the next versions gradient functions will be suported, so the velocities would be updated using the gradient of the function.

Each particle in the swarm represents a potential solution to the problem and moves through the search space by adjusting its position based on its own experience and that of its neighbors/population. The position of a particle in the search space is represented by a vector of parameters that define the solution.

The PSO algorithm works by evaluating the cost/fitness value of each particle (solution), which is a measure of how well its position solves the problem. The objective function is typically defined by the user and is specific to the problem being solved. The goal of the algorithm is to find the position that produces the optimal objective function value.

The movement of each particle is controlled by two components: the cognitive component and the social component. The cognitive component reflects the particle's personal experience, while the social component reflects the experience of the particles in its neighborhood or the entire population of particles. The two components are combined to determine the new velocity of the particle.

The formula for updating the velocity of a particle in the PSO algorithm is given by:

```
v_i(t+1) = w * v_i(t) + c1 * rand() * (pbest_i - x_i(t)) + c2 * rand() * (gbest - x_i(t))
```

where v_i(t) is the velocity of particle i at time t, x_i(t) is the current position of particle i at time t, pbest_i is the best position of particle i so far, gbest is the best position found by any particle in the swarm, w is the inertia weight, and c1 and c2 are the cognitive and social parameters, respectively. rand() is a random number generator that produces values between 0 and 1.

The formula for updating the position of a particle in the PSO algorithm is given by:

```
x_i(t+1) = x_i(t) + v_i(t+1)
```

where ```x_i(t)``` is the current position of particle i at time t, and ```v_i(t+1)``` is the new velocity of particle i at time ```t+1```.

The PSO algorithm continues iterating until a stopping criterion is met, such as a maximum number of iterations.

In summary, the PSO algorithm is a powerful optimization algorithm that can be used to find optimal solutions to a wide range of problems. By simulating the behavior of a swarm of particles, the algorithm is able to efficiently explore the search space and converge to the optimal solution. The cognitive and social components of the algorithm allow each particle to learn from its own experience and that of its neighbors, leading to a robust and efficient search.


### **References** 

- J. Kennedy and R. Eberhart, "Particle swarm optimization," Proceedings of ICNN'95 - International Conference on Neural Networks, Perth, WA, Australia, 1995, pp. 1942-1948 vol.4, doi: 10.1109/ICNN.1995.488968.

- Wang, D., Tan, D. & Liu, L. Particle swarm optimization algorithm: an overview. Soft Comput 22, 387–408 (2018). https://doi.org/10.1007/s00500-016-2474-6