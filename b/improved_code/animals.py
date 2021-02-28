from typing import Optional, Dict


class Animals:
    run_energy: Optional[int] = None
    swim_energy: Optional[int] = None
    fly_energy: Optional[int] = None

    def __init__(self, name: str, energy: int = 100, init_parameters: Dict = {}):
        self.name = init_parameters.get('name', name)
        self.energy = init_parameters.get('energy', energy)

    def say(self):
        print(f"Hello, I'm {self.__class__.__name__} and my name is {self.name}")

    def run(self):
        if self.run_energy:
            print("My name is "+str(self.name)+" and I running")
            self.energy = self.energy - self.run_energy
        else:
            print(f"My name is {self.name} and I can't run")

    def swim(self):
        if self.swim_energy:
            print(f"My name is {self.name} and I swimming")
            self.energy = self.energy - self.swim_energy
        else:
            print(f"My name is {self.name} and I can't swim")

    def fly(self):
        if self.fly_energy:
            print(f"My name is {self.name} and I flying")
            self.energy = self.energy - self.fly_energy
        else:
            print(f"My name is {self.name} and I can't fly")

    def get_energy(self):
        return self.energy
