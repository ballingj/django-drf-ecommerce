# Sample tests

def test_example():
    assert 1 == 1

def inc(x):
    return x + 1

def test_answer():
    assert inc(4) == 5  # will fail: 4 == 5
