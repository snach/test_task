from b.improved_code.fishes import Fish, FishCanFly


class TestFishes:
    def setup(self):
        self.fish = Fish('test_fish')

    def test_constructor(self):
        assert self.fish.name == 'test_fish'
        assert self.fish.energy == 100

    def test_say(self, capsys):
        self.fish.say()
        captured = capsys.readouterr()
        assert captured.out == "Hello, I'm Fish and my name is test_fish\n"
        assert self.fish.energy == 100

    def test_run(self, capsys):
        self.fish.run()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_fish and I can't run\n"
        assert self.fish.energy == 100

    def test_swim(self, capsys):
        self.fish.swim()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_fish and I swimming\n"
        assert self.fish.energy == 95

    def test_fly(self, capsys):
        self.fish.fly()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_fish and I can't fly\n"
        assert self.fish.energy == 100


class TestFishCanFly:
    def setup(self):
        self.fish = FishCanFly('test_fish_can_fly')

    def test_constructor(self):
        assert self.fish.name == 'test_fish_can_fly'
        assert self.fish.energy == 100

    def test_say(self, capsys):
        self.fish.say()
        captured = capsys.readouterr()
        assert captured.out == "Hello, I'm FishCanFly and my name is test_fish_can_fly\n"
        assert self.fish.energy == 100

    def test_run(self, capsys):
        self.fish.run()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_fish_can_fly and I can't run\n"
        assert self.fish.energy == 100

    def test_swim(self, capsys):
        self.fish.swim()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_fish_can_fly and I swimming\n"
        assert self.fish.energy == 95

    def test_fly(self, capsys):
        self.fish.fly()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_fish_can_fly and I flying\n"
        assert self.fish.energy == 80
