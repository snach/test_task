from .animals import Animals


class Fish(Animals):
    swim_energy = 5


class FishCanFly(Fish):
    fly_energy = 20
