from b.improved_code.dogs import Dog


class TestDogs:
    def setup(self):
        self.dog = Dog('test_dog')

    def test_constructor(self):
        assert self.dog.name == 'test_dog'
        assert self.dog.energy == 100

    def test_say(self, capsys):
        self.dog.say()
        captured = capsys.readouterr()
        assert captured.out == "Hello, I'm Dog and my name is test_dog\n"
        assert self.dog.energy == 100

    def test_run(self, capsys):
        self.dog.run()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_dog and I running\n"
        assert self.dog.energy == 90

    def test_swim(self, capsys):
        self.dog.swim()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_dog and I swimming\n"
        assert self.dog.energy == 70

    def test_fly(self, capsys):
        self.dog.fly()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_dog and I can't fly\n"
        assert self.dog.energy == 100
