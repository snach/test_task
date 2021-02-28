from b.improved_code.animals import Animals


class TestAnimals:

    def test_constructor(self):
        simple_animal = Animals('test', 999)
        assert simple_animal.name == 'test' and simple_animal.energy == 999

        animal_without_energy = Animals('test')
        assert animal_without_energy.name == 'test' and animal_without_energy.energy == 100

        animal_name_from_dict = Animals('test', 99, {'name': 'test_1'})
        assert animal_name_from_dict.name == 'test_1' and animal_name_from_dict.energy == 99

        animal_energy_from_dict = Animals('test', 99, {'energy': 999})
        assert animal_energy_from_dict.name == 'test' and animal_energy_from_dict.energy == 999

    def test_say(self, capsys):
        animal = Animals('test_animal')
        animal.say()
        captured = capsys.readouterr()
        assert captured.out == "Hello, I'm Animals and my name is test_animal\n"

    def test_action_energy_none(self):
        animal = Animals('test', 100)
        animal.say()
        animal.run()
        animal.swim()
        animal.fly()
        assert animal.get_energy() == 100
