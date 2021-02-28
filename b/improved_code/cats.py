from typing import Dict
from .animals import Animals


class Cat(Animals):
    run_energy = 5


class Tiger(Animals):
    run_energy = 20
    swim_energy = 40

    def __init__(self, name: str, energy: int = 200, init_parameters: Dict = {}):
        super(Tiger, self).__init__(name=name, energy=energy, init_parameters=init_parameters)
