from typing import Union
import numpy as np


class Particle:

    def __init__(self, n_dimensions: int, min_x: list[Union[int, float]], max_x: list[Union[int, float]]) -> None:
        self.n_dimensions = n_dimensions
        self.min_x = np.array(min_x)
        self.max_x = np.array(max_x)
        self.position = self.initialize()
        self.velocity = self.initialize()
        self.best_position = self.position
        self.best_objective_value = None

    def initialize(self) -> np.array:
        return self.min_x + (self.max_x - self.min_x) * np.array([np.random.rand() for _ in range(self.n_dimensions)])
    
    def get_n_dimensions(self) -> int:
        return self.n_dimensions

    def get_min_x(self) -> np.array:
        return self.min_x

    def get_max_x(self) -> np.array:
        return self.max_x

    def set_position(self, position: np.array) -> None:
        self.position = position

    def get_position(self) -> np.array:
        return self.position

    def set_velocity(self, velocity: np.array) -> None:
        self.velocity = velocity

    def get_velocity(self) -> np.array:
        return self.velocity
    
    def set_best_position(self, best_position: np.array) -> None:
        self.best_position = best_position

    def get_best_position(self) -> np.array:
        return self.best_position

    def set_best_objective_value(self, best_objective_value: Union[int, float]) -> None:
        self.best_objective_value = best_objective_value   

    def get_best_objective_value(self) -> Union[int, float]:
        return self.best_objective_value

    def move_particle(self) -> None:
        updated_position = self.position + self.velocity
        # consider the x min and max limits
        updated_position = np.where(updated_position < self.min_x, self.min_x, updated_position)
        updated_position = np.where(updated_position > self.max_x, self.max_x, updated_position)
        self.position = updated_position