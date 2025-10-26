# app.py
# This is a test commit
# Adding a commit to check the github hosted runner
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
