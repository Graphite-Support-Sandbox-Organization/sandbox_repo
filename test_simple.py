"""Simple smoke tests for the sandbox repo."""

import unittest


def greet(name: str) -> str:
    return f"Hello, {name}!"


class TestGreet(unittest.TestCase):
    def test_greet_returns_hello_message(self):
        self.assertEqual(greet("Graphite"), "Hello, Graphite!")

    def test_greet_handles_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
