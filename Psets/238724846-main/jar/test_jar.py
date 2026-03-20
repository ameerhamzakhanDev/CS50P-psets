from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""


def test_withdraw():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.withdraw(1)
    assert str(jar) == ""

# wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png
