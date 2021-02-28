from b.improved_code.cats import Cat, Tiger


class TestCats:
    def setup(self):
        self.cat = Cat('test_cat')

    def test_constructor(self):
        assert self.cat.name == 'test_cat'
        assert self.cat.energy == 100

    def test_say(self, capsys):
        self.cat.say()
        captured = capsys.readouterr()
        assert captured.out == "Hello, I'm Cat and my name is test_cat\n"
        assert self.cat.energy == 100

    def test_run(self, capsys):
        self.cat.run()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_cat and I running\n"
        assert self.cat.energy == 95

    def test_swim(self, capsys):
        self.cat.swim()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_cat and I can't swim\n"
        assert self.cat.energy == 100

    def test_fly(self, capsys):
        self.cat.fly()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_cat and I can't fly\n"
        assert self.cat.energy == 100


class TestTiger:
    def setup(self):
        self.tiger = Tiger('test_tiger')

    def test_constructor(self):
        assert self.tiger.name == 'test_tiger'
        assert self.tiger.energy == 200

    def test_say(self, capsys):
        self.tiger.say()
        captured = capsys.readouterr()
        assert captured.out == "Hello, I'm Tiger and my name is test_tiger\n"
        assert self.tiger.energy == 200

    def test_run(self, capsys):
        self.tiger.run()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_tiger and I running\n"
        assert self.tiger.energy == 180

    def test_swim(self, capsys):
        self.tiger.swim()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_tiger and I swimming\n"
        assert self.tiger.energy == 160

    def test_fly(self, capsys):
        self.tiger.fly()
        captured = capsys.readouterr()
        assert captured.out == "My name is test_tiger and I can't fly\n"
        assert self.tiger.energy == 200
