import time
import numpy as np
from matplotlib import pyplot as plt
from src.particle import Particle


class ParticleSwarmOptimizer(Particle):

    def __init__(self, objective: callable, sense: str, n_dimensions: int, min_x: float, max_x: float, n_particles: int = 20, 
                 n_iterations: int = 50, w: float = 0.75, c1: float = 0.8, c2: float = 0.9, constraints: list[callable] = []) -> None:

        self.objective = objective
        self.sense = 0 if sense == 'min' else 1
        self.n_dimensions = n_dimensions
        self.min_x = min_x
        self.max_x = max_x
        self.n_particles = n_particles
        self.n_iterations = n_iterations
        self.w = w
        self.c1 = c1
        self.c2 = c2

        self.constraints = constraints

        self.particles = [Particle(self.get_n_dimensions(), self.get_min_x(), self.get_max_x()) for _ in range(n_particles)]
        
        self.best_objective_value = 1e21 if self.get_sense() == 0 else -1e21

        for particle in self.get_particles():
            particle.set_best_objective_value(self.get_best_objective_value())

        self.best_position = self.particles[0].get_position()

        self.objective_values = []

    def get_particles(self) -> list[Particle]:
        return self.particles

    def get_sense(self) -> bool:
        return self.sense
    
    def get_constraints(self) -> list[callable]:
        return self.constraints

    def get_objective_values(self):
        return self.objective_values

    def add_objective_value(self) -> None:
        self.objective_values += self.get_best_objective_value(),

    def evalute_solution(self, solution: np.array) -> float:
        return self.objective(solution)

    def is_feasible(self, solution: list[float]) -> bool:
        for constraint in self.get_constraints():
            if not constraint(solution):
                return False                
        return True

    def update_best_solutions(self) -> None:

        for particle in self.get_particles():

            current_position = particle.get_position()

            particle_objective_value = self.evalute_solution(current_position)

            if self.sense == 0:
                condition_local = particle_objective_value < particle.get_best_objective_value()
                condition_global = particle_objective_value < self.get_best_objective_value()
            else:
                condition_local = particle_objective_value > particle.get_best_objective_value()
                condition_global = particle_objective_value > self.get_best_objective_value()

            if not self.is_feasible(current_position):
                continue

            if condition_local:
                particle.set_best_position(current_position)
                particle.set_best_objective_value(particle_objective_value)

            if condition_global:
                self.set_best_position(current_position)
                self.set_best_objective_value(particle_objective_value)
                
    def move_particle(self, particle: Particle) -> None:

        r1, r2 = np.random.rand(), np.random.rand()

        updated_velocity = self.w * particle.get_velocity() + \
            self.c1 * r1 * (particle.get_best_position() - particle.get_position()) + \
                        self.c2 * r2 * (self.get_best_position() - particle.get_position())

        particle.set_velocity(updated_velocity)
        particle.move_particle()

    def move_particles(self) -> None:
        for particle in self.get_particles():
            self.move_particle(particle)        

    def run(self) -> None:

        iter_counter = 0

        while iter_counter < self.n_iterations:
            iter_counter += 1

            self.move_particles()
            self.update_best_solutions()
            self.add_objective_value()
    
        if not self.is_feasible(self.get_best_position()):
            print("No feasible solution found.")
            self.best_position = np.array([np.nan, np.nan])

    def plot_search(self) -> None:
        plt.plot(self.get_objective_values())
        plt.ylabel('Objective value')
        plt.xlabel('Step')
        plt.show()