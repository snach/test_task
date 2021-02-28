from b.improved_code.ducks import Duck


class TestDucks:
    def setup(self):
        self.duck = Duck('test_duck')

    def test_constructor(self):
        assert self.duck.name == 'test_duck'
        assert self.duck.energy == 100

    def test_say(self, capsys):
        self.duck.say()
        captured = capsys.readouterr()
        assert captured.out == "Hello, I'm Duck and my name is test_duck\n"
        assert self.duck.energy == 100

    def test_run(self, capsys):
        self.duck.run()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_duck and I can't run\n"
        assert self.duck.energy == 100

    def test_swim(self, capsys):
        self.duck.swim()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_duck and I swimming\n"
        assert self.duck.energy == 90

    def test_fly(self, capsys):
        self.duck.fly()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_duck and I flying\n"
        assert self.duck.energy == 70
