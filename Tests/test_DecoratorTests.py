import unittest
from Decorator.decorator import do_twice
import pprint


@do_twice
def say_whee():
    print("Whee....!")


@do_twice
def say_hello():
    print("Hello")


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_decorate(self):
        say_whee()


if __name__ == '__main__':
    unittest.main()