"""A simple, self-contained Python test script.

Run it directly with `python test_sample.py` or via `pytest test_sample.py`.
"""


def add(a, b):
    return a + b


def is_palindrome(text):
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")


def _run():
    tests = [test_add, test_is_palindrome]
    failures = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
        except AssertionError as exc:
            failures += 1
            print(f"FAIL: {test.__name__}: {exc}")
    if failures:
        print(f"\n{failures} test(s) failed.")
    else:
        print(f"\nAll {len(tests)} test(s) passed.")
    return failures


if __name__ == "__main__":
    raise SystemExit(_run())
