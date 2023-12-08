import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")
    with pytest.raises(ValueError):
        assert convert("20/5")
    with pytest.raises(ValueError):
        assert convert("pig/frog")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    assert gauge(30) == "30%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

if __name__ == "__main__":
    main()
